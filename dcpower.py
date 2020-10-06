import requests
import json

parameters = {'itemsPerPage': '42',
            'contractLengthMin': '1',
            'contractLengthMax': '36',
            'rateMin': '0',
            'rateMax': '0.2'}

main_url = 'https://edocket.dcpsc.org/apis/api/retail-choice/offers/'
response = requests.get(main_url, params=parameters)
to_extract = json.loads(response.text)
for needed_info in to_extract['data']:
    plans = {'supplierOfferingId': needed_info['supplierOfferingId']}
    url = 'https://edocket.dcpsc.org/apis/api/retail-choice/offers/{}'.format(plans['supplierOfferingId'])
    # print(url)
    response1 = requests.get(url, params=parameters)
    plans_data = json.loads(response1.text)
    # print(plans_data['fees'])
    if len(plans_data['fees'])!=0:
        fee_description = plans_data['fees'][0]['feeDescription']
        fee_amount = plans_data['fees'][0]['feeAmt']
    else:
        fee_description = None
        fee_amount = None
    plans_info = {
                'PlanName': plans_data['planName'],
                'TermMonths': plans_data['termMonths'],
                'CompanyName': plans_data['companyName'],
                'RateAmt': plans_data['rateAmt'],
                'RateTypeName': plans_data['rateTypeName'],
                'Fee': [{'fee_description': fee_description,
                            'fee_amount': fee_amount}]}

    print(plans_info)