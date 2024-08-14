import json
from flask import Flask, request, Response
from VendingMachine import VendingMachine

vend_o_matic = VendingMachine()

app = Flask(__name__)

@app.put("/")
def add_coin():
    args = request.get_json()
    amount = args.get('coin')
    if amount != 1:
        return "You can add exactly one coin per request.", 403
    current_coins = vend_o_matic.add_coin(amount)
    res = Response(status=204)
    res.headers['X-Coins'] = current_coins
    return res

@app.delete("/")
def remove_coin():
    coins = vend_o_matic.remove_coins(True)
    res = Response(status=204)
    res.headers['X-Coins'] = coins
    return res

@app.get("/inventory")
def get_all_inventory():
    return vend_o_matic.get_all_inventory()

@app.get("/inventory/<item_id>")
def get_inventory_by_id(item_id):
    remaining_inventory = vend_o_matic.get_inventory_by_id(item_id)
    return [remaining_inventory]

@app.put("/inventory/<item_id>")
def dispense_items(item_id):
    coins = vend_o_matic.current_coins
    if vend_o_matic.get_inventory_by_id(item_id) == 0:
        res = Response(status=404)
        res.headers['X-Coins'] = coins
        return res
    if coins < 2:
        res = Response(status=403)
        res.headers['X-Coins'] = coins
        return res
    
    result = vend_o_matic.transact(item_id)
    res = Response(json.dumps({'quantity': result['quantity']}), status=200, mimetype="application/json")
    res.headers['X-Coins'] = result['coins_to_return']
    res.headers['X-Inventory-Remaining'] = result['inventory_remaining']
    return res
