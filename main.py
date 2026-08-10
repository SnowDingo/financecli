import typer
import currency

app = typer.Typer()

@app.command("Home")
def main():
    """
    Run the main FinanceCLI app
    """
    print("FINANCE CLI")

@app.command("calcfx")
def calcFX(original: str, convertcurrency: str):
    """
    Converts certain amount of one currency to another
    """
    exchangerate = currency.fetchCurrentExchangeRate(original,convertcurrency)
    print(f"The exchange rate of {original} to {convertcurrency} is {str(exchangerate)}")

if __name__ == "__main__":
    app()
