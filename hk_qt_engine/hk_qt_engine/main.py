from fastapi import FastAPI

app = FastAPI()

def calculate_max_value(income: int) -> int:
    if income <= 2999:
        return 0.15 * income
    
    if 2999 < income <= 5999:
        return 0.25 * income
    
    if 5999 < income <= 8999:
        return 0.35 * income
    
    if 8999 < income <= 14999:
        return 0.45 * income
    
    return 0.5 * income

@app.get("/calculate")
async def root(income: int):
    return {
        "max_value": calculate_max_value(income),
    }