import typer
import currency
import datetime
import pytz

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
    Shows the conversion rate of the first argument's current to another
    """
    exchangerate = currency.fetchCurrentExchangeRate(original,convertcurrency)
    print(f"The exchange rate of {original} to {convertcurrency} is {str(exchangerate)}")

@app.command("timezone")
def calcTimezone():
    date = datetime.datetime.now()
    print(f"now: " + date.strftime("%b") + " " + date.strftime("%d") + " " + date.strftime("%H") + ":" + date.strftime("%S"))
    datenow = datetime.datetime.now(pytz.utc)
    # Time zones
    tz_ny = pytz.timezone('America/New_York')
    tz_london = pytz.timezone('Europe/London')
    tz_japan = pytz.timezone('Asia/Tokyo')
    tz_china = pytz.timezone('Asia/Shanghai')
    # convert to each local timezones
    now_ny = datenow.astimezone(tz_ny)
    now_lo = datenow.astimezone(tz_london)
    now_jp = datenow.astimezone(tz_japan)
    now_bj = datenow.astimezone(tz_china)
    fmt = "%b %d %H:%M"
    print("\n=AROUND THE WORLD=")
    print("UTC: " + datenow.strftime(fmt))
    print("Tokyo Japan: " + now_jp.strftime(fmt))
    print("London UK: " + now_lo.strftime(fmt))
    print("New York USA: " + now_ny.strftime(fmt))
    print("Bejing China: " +now_bj.strftime(fmt))
    return

if __name__ == "__main__":
    app()
