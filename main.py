from olx.asgi import application
import uvicorn




if __name__=="__main__":
    uvicorn.run(application,port=7000)