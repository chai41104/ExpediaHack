import json
def returnFixDate(content) :
    return json.dumps(
        [{
            'period': content['reservation'],
            'price': "$25",
            'id': "11111"
        }]
    )

def returnFlexibleDate(content) :
    return json.dumps(
        [{
            'period': '11/08/2018 - 11/08/2018',
            'price': "$25",
            'id': "11111"
        },{
            'period': '12/08/2018 - 12/08/2018',
            'price': "$32",
            'id': "11111"
        },{
            'period': '8/08/2018 - 8/08/2018',
            'price': "$67",
            'id': "11111"
        },{
            'period': '9/08/2018 - 9/08/2018',
            'price': "$45",
            'id': "11111"
        },{
            'period': '10/08/2018 - 10/08/2018',
            'price': "$36",
            'id': "11111"
        }]
    )