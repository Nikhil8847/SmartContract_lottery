from brownie import accounts, Lottery, network, config, web3
from web3 import Web3


def test_get_entrace_fee():
    account = accounts[0]
    lottery = Lottery.deploy(
        config["networks"][network.show_active()]["eth_usd_price_feed"],
        {"from": account},
    )
    # print(lottery.getEntranceFee())
    assert lottery.getEntranceFee() > Web3.toWei(0.020, "ether")
    assert lottery.getEntranceFee() < Web3.toWei(0.022, "ether")
