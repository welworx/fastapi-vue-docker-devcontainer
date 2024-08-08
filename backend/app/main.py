from http import HTTPStatus
from os import environ

from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from neo4j import GraphDatabase

app = FastAPI()

BACKEND_URL = environ.get("BACKEND_URL", "http://localhost:3000")
FRONTEND_URL = environ.get("FRONTEND_URL", "http://localhost:8080")

NEO4J_URI = environ.get("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = environ.get("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = environ.get("NEO4J_PASSWORD", "password")
NEO4J_DB = environ.get("NEO4J_DB", "neo4j")


# Ensure that you don't get blocked by CORS policy
origins = ["http://localhost", FRONTEND_URL, BACKEND_URL]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Query Neo4j database
def query(cypher_str):
    with GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD)) as driver:
        driver.verify_connectivity()
        records = driver.execute_query(cypher_str, database_=NEO4J_DB)
        records_dict = [rec.data() for rec in records]
    driver.close()

    if len(records_dict) == 0:
        return Response(status_code=HTTPStatus.NO_CONTENT)

    return records_dict


@app.get("/")
async def get_persons():

    cypher_str = """
    MATCH (p:Person)
    RETURN distinct p.name as Name, p.born as YearBorn
    LIMIT 100"""

    return query(cypher_str)
