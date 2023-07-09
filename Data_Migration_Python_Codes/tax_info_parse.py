import json

def parse1():
    parsed_data = json.load(open('data_from_qb_taxrate_PR.json'))

    final_dict = dict()
    for item in parsed_data:
        name = None
        description = None
        ratevalue = None

        if "Name" in item:
            name = item["Name"]
        
        if "Description" in item:
            description = item["Description"]
        
        if "RateValue" in item:
            ratevalue = item["RateValue"]

        if not ratevalue:
            if "EffectiveTaxRate" in item:
                EffectiveTaxRate = item["EffectiveTaxRate"][-1]
                if "RateValue" in EffectiveTaxRate:
                    ratevalue = EffectiveTaxRate["RateValue"]
                else:
                    ratevalue = 0
            else:
                ratevalue = 0

        final_dict[item['Id']] = [name,description,ratevalue]

    mapped_data = json.dumps(final_dict,indent=4)
    with open('tax_id_and_name_PR.json','w') as f:
        f.write(mapped_data)

parse1()