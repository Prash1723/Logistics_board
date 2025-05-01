from cal import inv_kpi
from rich.console import Console

rc = Console()

bot = inv_kpi(10, 12, 4, 40, 50000)

if __name__ == "__main__":
    x = bot.run()
    for k, v in x.values():
        rc.print(k+" :", v, style="yellow")
