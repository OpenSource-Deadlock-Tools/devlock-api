
from fastapi import FastAPI, Request

from app import metrics
from app.datarepo import repo
from app.limiter import limiter

v1 = FastAPI()

@v1.get("/matches")
@limiter.limit("100/minute")
async def match_list(request: Request, skip: int = 0):
    metrics.api_called('GET', '/matches')

    query_result = repo.query('SELECT * FROM match_info LIMIT 20 OFFSET %(offset)s', {'offset': skip})
    return query_result.named_results()


@v1.get("/matches/{matchId}/meta")
@limiter.limit("100/minute")
async def match_meta(request: Request, matchId: str):
    metrics.api_called('GET', '/matches/{matchId}/meta')
    query_result = repo.query('SELECT * FROM match_info WHERE match_id = %(matchId)s', {'matchId': matchId})
    return query_result.first_item


@v1.get("/active-matches")
@limiter.limit("100/minute")
async def active_matches(request: Request, skip: int = 0):
    metrics.api_called('GET', '/active-matches')
    query_result = repo.query('SELECT * FROM summary_active_matches LIMIT 500 OFFSET %(skip)s', {'skip': skip})
    return query_result.named_results()
