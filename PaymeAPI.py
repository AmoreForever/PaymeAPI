#  ______   ______     __  __     __    __     ______        ______     ______   __    
# /\  == \ /\  __ \   /\ \_\ \   /\ "-./  \   /\  ___\      /\  __ \   /\  == \ /\ \   
# \ \  _-/ \ \  __ \  \ \____ \  \ \ \-./\ \  \ \  __\      \ \  __ \  \ \  _-/ \ \ \  
#  \ \_\    \ \_\ \_\  \/\_____\  \ \_\ \ \_\  \ \_____\     \ \_\ \_\  \ \_\    \ \_\ 
#   \/_/     \/_/\/_/   \/_____/   \/_/  \/_/   \/_____/      \/_/\/_/   \/_/     \/_/ 
                                                                                     
# :copyright: (c) 2022-2023 by Amore.
# :license: MIT, see LICENSE for more details.

                      
import requests

class Payme:
    headers = {'device': '6Fk1rB', 'user-agent': 'Mozilla/57.36'}

    def __init__(self, mycard):
        self.mycard = mycard

    def create(self, summ, desc):
        summa = summ * 100
        response = requests.post('https://payme.uz/api/p2p.create',
                                 json={"method": "p2p.create",
                                       "params": {"card_id": self.mycard,
                                                  "amount": summa,
                                                  "description": desc}},
                                 headers=self.headers,
                                 timeout=10)


        if response.status_code != 200:
            return {'ok': False, 'error': f'HTTP error {response.status_code}'}

        data = response.json()
        return (
            {
                'ok': True,
                'result': {
                    'id': data['result']['cheque'].get('_id'),
                    'amount': f'{summ} UZS',
                    'pay_url': f'https://checkout.paycom.uz/{data["result"]["cheque"].get("_id")}',
                },
            }
            if "result" in data
            else {'ok': False, 'error': data['error']}
        )

    def info(self, check_id):
        response = requests.post('https://payme.uz/api/cheque.get',
                                 json={"method": "cheque.get", "params": {"id": check_id}},
                                 headers=self.headers,
                                 timeout=10)


        if response.status_code != 200:
            return {'ok': False, 'error': f'HTTP error {response.status_code}'}

        data = response.json()
        cheque = data['result']['cheque']['pay_time']
        recipient = data['result']['cheque']['account'][1]['value']
        org = data['result']['cheque']['merchant']['organization']
        return {
            'ok': True,
            'org': org,
            'recipient': recipient,
            'payment': 'successfully'
            if bool(cheque)
            else 'unsuccessfully',
        }
