import fastapi
import rollbar
from rollbar.contrib.fastapi import add_to as rollbar_add_to

# Initialize Rollbar SDK with your server-side access token
rollbar.init('a1c73ddb60dd4267ac4c3da541ec92d5')

# Integrate Rollbar with FastAPI application before adding routes to the app
app = fastapi.FastAPI()
rollbar_add_to(app)

# Add an /error endpoint to cause an uncaught exception
async def localfunc(arg1, arg2, arg3):
    # Both local variables and function arguments will be sent to Rollbar
    # and available in the UI
    localvar = 'local variable'
    cause_error_with_local_variables

@app.get('/error')
async def read_error():
    await localfunc('func_arg1', 'func_arg2', 1)
    