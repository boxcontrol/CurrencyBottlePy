from bottle import error, run, request, static_file, route, TEMPLATE_PATH, jinja2_view
import requests 
import collections

TEMPLATE_PATH[:] = ['templates']

values = {'USD': 'US Dollar', 
        'EUR': 'Euro', 
        'GBP': 'British Pound', 
        'AED': 'UAE Dircham',
        'AFN': 'Afghanistan Afghani',
        'ALL': 'Albanian Lek',
        'DZD': 'Algerian Dinar',
        'ADF': 'Andorran Franc',
        'ADP': 'Andorran Peseta',
        'AOA': 'Angolan Kwanza',
        'AON': 'Angolan New Kwanza',
        'ARS': 'Argentine Peso',
        'AMD': 'Armenian Dram',
        'AWG': 'Aruban Florin',
        'AUD': 'Australian Dollar',
        'ATS': 'Austrian Schilling',
        'AZM': 'Azerbaijan New Manat',
        'BSD': 'Bahamian Dollar',
        'BHD': 'Bahraini Dinar',
        'BDT': 'Barbados Dollar',
        'BYR': 'Belarusian Ruble',
        'BEF': 'Belgian Franc',
        'BZD': 'Belize Dollar',
        'BMD': 'Bermudian Dollar',
        'BTN': 'Bhutan Ngultrum',
        'BOB': 'Bolivian Boliviano',
        'BAM': 'Bosnian Mark',
        'BWP': 'Botswana Pula',
        'BRL': 'Brazilian Real',
        'BND': 'Brunei Dollar',
        'BGN': 'Bulgarian Lev',
        'BIF': 'Burundi Franc',
        'KHR': 'Cambodian Riel',
        'CAD': 'Canadian Dollar',
        'CVE': 'Cape Verde Escudo',
        'KYD': 'Cayman Islands Dollar',
        'XOF': 'CFA Franc BCEAO',
        'XAF': 'CFA Franc BEAC',
        'XPF': 'CFP Franc',
        'CLP': 'Chilean Peso',
        'CNY': 'Chinese Yuan Renminbi',
        'COP': 'Colombian Peso',
        'KMF': 'Comoros Franc',
        'CDF': 'Congolese Franc',
        'CRC': 'Costa Rican Colon',
        'HRK': 'Croatian Kuna',
        'CUC': 'Cuban Convertible Peso',
        'CUP': 'Cuban Peso',
        'CYP': 'Cyprus Pound',
        'CZK': 'Czech Koruna',
        'DKK': 'Danish Krone',
        'DJF': 'Djibouti Franc',
        'DOP': 'Dominican R. Peso',
        'NLG': 'Dutch Guilder',
        'XCD': 'East Caribbean Dollar',
        'XEU': 'ECU',
        'ECS': 'Ecuador Sucre',
        'EGP': 'Egyptian Pound',
        'SVC': 'El Salvador Colon',
        'EEK': 'Estonian Kroon',
        'ETB': 'Ethiopian Birr',
        'FKP': 'Falkland Islands Pound',
        'FJD': 'Fiji Dollar',
        'FIM': 'Finnish Markka',
        'FRF': 'French Franc',
        'GMD': 'Gambian Dalasi',
        'GEL': 'Georgian Lari',
        'DEM': 'German Mark',
        'GHC': 'Ghanaian Cedi',
        'GHS': 'Ghanaian New Cedi',
        'GIP': 'Gibraltar Pound',
        'XAU': 'Gold(oz.)',
        'GRD': 'Greek Drachma',
        'GTQ': 'Guatemalan Quetzal',
        'GNF': 'Guinea Franc',
        'GYD': 'Guyanese Dollar',
        'HTG': 'Haitian Gourde',
        'HNL': 'Honduran Lempira',
        'HKD': 'Hong Kong Dollar',
        'HUF': 'Hungarian Forint',
        'ISK': 'Iceland Krona',
        'INR': 'Indian Rupee',
        'IDR': 'Indonesian Rupiah',
        'IRR': 'Iranian Rial',
        'IQD': 'Iraqi Dinar',
        'IEP': 'Irish Punt',
        'ILS': 'Israeli New Shekel',
        'ITL': 'Italian Lira',
        'JMD': 'Jamaican Dollar',
        'JPY': 'Japanese Yen',
        'JOD': 'Jordanian Dinar',
        'KZT': 'Kazakhstan Tenge',
        'KES': 'Kenyan Shilling',
        'KWD': 'Kuwaiti Dinar',
        'KGS': 'Kyrgyzstanian Som',
        'LAK': 'Lao Kip',
        'LVL': 'Latvian Lats',
        'LBP': 'Lebanese Pound',
        'LSL': 'Lesotho Loti',
        'LRD': 'Liberian Dinar',
        'LYD': 'Lybian Dinar',
        'LTL': 'Lithuanian Litas',
        'LUF': 'Luxembourg Franc',
        'MOP': 'Macau Pataca',
        'MKD': 'Macedonian Denar',
        'MGA': 'Malagasy Ariary',
        'MGF': 'Malagasy Franc',
        'MWK': 'Malawi Kwacha',
        'MYR': 'Malaysian Ringgit',
        'MVR': 'Maldive Rufiyaa',
        'MTL': 'Maltese Lira',
        'MRO': 'Mauritanian Ouguiya',
        'MUR': 'Mauritius Rupee',
        'MXN': 'Mexican Peso',
        'MDL': 'Moldovan Leu',
        'MNT': 'Mongolian Tugrik',
        'MAD': 'Moroccan Dirham',
        'MZM': 'Mozambique Metical',
        'MZN': 'Mozambique New Metical',
        'MMK': 'Myanmar Kyat',
        'NAD': 'Namibia Dollar',
        'NPR': 'Nepalese Rupee',
        'NZD': 'New Zealand Dollar',
        'NIO': 'Nicaraguan Cordoba Oro',
        'NGN': 'Nigerian Naira',
        'ANG': 'NL Antillian Guilder',
        'KPW': 'North Korean Won',
        'NOK': 'Norwegian Kroner',
        'OMR': 'Omani Rial',
        'PKR': 'Pakistan Rupee',
        'XPD': 'Palladium(oz.)',
        'PAB': 'Panamanian Balboa',
        'PGK': 'Papua New Guinea Kina',
        'PYG': 'Paraguay Guarani',
        'PEN': 'Peruvian Nuevo Sol',
        'PHP': 'Philippine Peso',
        'XPT': 'Platinum (oz.)',
        'PLN': 'Polish Zloty',
        'PTE': 'Portuguese Escudo',
        'QAR': 'Qatari Rial',
        'ROL': 'Romanian Lei',
        'RON': 'Romanian New Lei',
        'RUB': 'Russian Rouble',
        'RWF': 'Rwandan Franc',
        'WST': 'Samoan Tala',
        'STD': 'Sao Tome/Principe Dobra',
        'SAR': 'Saudi Riyal',
        'RSD': 'Serbian Dinar',
        'SCR': 'Seychelles Rupee',
        'SLL': 'Sierra Leone Leone',
        'XAG': 'Silver (oz.)',
        'SGD': 'Singapore Dollar',
        'SKK': 'Slovak Koruna',
        'SIT': 'Slovenian Tolar',
        'SBD': 'Solomon Islands Dollar',
        'SOS': 'Somali Shilling',
        'ZAR': 'South African Rand',
        'KRW': 'South-Korean Won',
        'ESP': 'Spanish Peseta',
        'LKR': 'Sri Lanka Rupee',
        'SHP': 'St. Helena Pound',
        'SDD': 'Sudanese Dinar',
        'SDP': 'Sudanese Old Pound',
        'SDG': 'Sudanese Pound',
        'SRD': 'Suriname Dollar',
        'SRG': 'Suriname Guilder',
        'SZL': 'Swaziland Lilangeni',
        'SEK': 'Swedish Krona',
        'CHF': 'Swiss Franc',
        'SYP': 'Syrian Pound',
        'TWD': 'Taiwan Dollar',
        'TZS': 'Tanzanian Shilling',
        'THB': 'Thai Baht',
        'TOP': "Tonga Pa'anga",
        'TTD': 'Trinidad/Tobago Dollar',
        'TND': 'Tunisian Dinar',
        'TRY': 'Turkish Lira',
        'TRL': 'Turkish Old Lira',
        'TMM': 'Turkmenistan Manat',
        'UGX': 'Uganda Shilling',
        'UAH': 'Ukraine Hryvnia',
        'UYU': 'Uruguayan Peso',
        'AED': 'Utd.Arab Emir. Dirham',
        'VUV': 'Vanuatu Vatu',
        'VEB': 'Venezuelan Bolivar',
        'VEF': 'Venezuelan Bolivar Fuerte',
        'VND': 'Vietnamese Dong',
        'YER': 'Yemeni Rial',
        'YUN': 'Yugoslav Dinar',
        'ZMK': 'Zambian Kwacha',
        'ZWD': 'Zimbabwe Dollar'
        }

@route('/static/css/<filename>')
def cssget(filename):
    return static_file(filename, root="./static/css")
    
@route('/static/js/<filename>')
def javaget(filename):
    return static_file(filename, root="./static/js")
    
@route('/static/fonts/<filename>')
def fontsget(filename):
    return static_file(filename, root="./static/fonts")

@route('/static/js/vendor/<filename>')
def modernget(filename):
    return static_file(filename, root="./static/js/vendor")

@route('/static/img/<filename>')
def faviconget(filename):
    return static_file(filename, root="./static/img")

@route('/', name='home', method='GET')
@jinja2_view('index.html')
def index():
    return {'title':'Home',
            'values': collections.OrderedDict(sorted(values.items()))}
   
@route('/result', method='POST') 
@jinja2_view('result.html')
def result():
    convert_from = request.forms.get('convert_from').upper()
    convert_to = request.forms.get('convert_to').upper()
    value_to_convert = request.forms.get('value_to_convert')
    url = ('http://convert.gfxsector.net/currency?from=%s&to=%s&q=1') % (convert_from, convert_to)
    rate = requests.get(url).json()['v']
    converted = float(value_to_convert)*float(requests.get(url).json()['v'])
    
    return {'rate':rate, 
            'converted':converted, 
            'title':'Result'}
    
@error(404)
@jinja2_view('404.html')
def error404(error):
    return {'title':'404'}

@error(500)
def error500(error):
    return 'Nothing here, sorry'
    
run(host='0.0.0.0', port=8081, debug=False)
