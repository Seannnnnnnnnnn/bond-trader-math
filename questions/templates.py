import random

class FuturesImpliedYield:
    name = "futures_implied_yield"

    @staticmethod
    def generate():
        price = random.randint(9500, 9850) / 100  # e.g., 95.25
        text = f"Futures price is {price:.2f}. What is the implied yield (in %)?"
        true_yield = (100 - price)  # simple model
        return {
            "type": FuturesImpliedYield.name,
            "text": text,
            "price": price,
            "true_yield": true_yield,
            "options": None  # free-text
        }


class BondEFP:
    name = "bond_efp"

    @staticmethod
    def generate():
        futures_price = random.randint(9500, 9900) / 100
        bond_yield = random.uniform(2.0, 5.0)

        efp = (100 - futures_price) - bond_yield

        text = (f"Futures price is {futures_price:.2f} and bond yield is "
                f"{bond_yield:.2f}%. What is the EFP (in bps)?")

        return {
            "type": BondEFP.name,
            "text": text,
            "futures_price": futures_price,
            "bond_yield": bond_yield,
            "efp": efp * 100,  # convert to bps
            "options": None
        }


class DV01Hedge:
    name = "dv01_hedge"

    @staticmethod
    def generate():
        dv01 = random.uniform(4.0, 9.0)  # per $1m notional
        trade_size = random.choice([25, 50, 75, 100])  # millions
        fut_dv01 = random.uniform(55, 75)  # dv01 per contract

        total_dv01 = dv01 * trade_size
        hedge_contracts = total_dv01 / fut_dv01

        text = (
            f"DV01 of the bond is {dv01:.2f} per $1m. "
            f"Client buys {trade_size}m face. "
            f"Futures DV01 is {fut_dv01:.1f}. "
            f"Do you buy or sell futures, and how many?"
        )

        # multiple choice
        choice = random.randint(0, 1)

        options = [
            f"Buy {round(hedge_contracts)} futures",
            f"Sell {round(hedge_contracts)} futures"
        ]

        return {
            "type": DV01Hedge.name,
            "text": text,
            "dv01": dv01,
            "trade_size": trade_size,
            "fut_dv01": fut_dv01,
            "hedge_contracts": hedge_contracts,
            "correct_side": "sell",  # if client buys bonds, trader sells futures
            "options": options
        }
