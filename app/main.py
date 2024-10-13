import os

from fastapi import FastAPI

from app.V1 import v1

app = FastAPI()
#app.mount("/metrics", metrics.metricApp)

# NOTE, these endpoints are just the few that are stable, more are in the pipeline but don't wanna publish them yet
app.mount('/v1', v1)


