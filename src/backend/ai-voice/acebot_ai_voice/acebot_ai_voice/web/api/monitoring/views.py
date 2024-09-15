from fastapi import APIRouter
from fastapi.responses import HTMLResponse


router = APIRouter()


@router.get("/health", response_class=HTMLResponse , tags=["Health"])
async def healthcheck():
    html_content = """ 
    <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>API Status</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    background-color: #f0f0f0;
                }
                .status-message {
                    font-size: 24px;
                    color: #4CAF50; /* Green color */
                    text-align: center;
                }
            </style>
        </head>
        <body>
            <div class="status-message">
                API is up and running
            </div>
        </body>
        </html>
    """
    return HTMLResponse(content=html_content)