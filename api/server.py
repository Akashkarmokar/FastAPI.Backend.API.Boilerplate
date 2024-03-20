import uvicorn
  

if __name__ == '__main__':
    uvicorn.run('main:app', host="protfolio_backend_api", port = 8086, reload=True)