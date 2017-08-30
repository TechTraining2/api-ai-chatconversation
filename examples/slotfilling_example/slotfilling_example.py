from __future__ import print_function
import os
import sys
import json

try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            os.pardir,
            os.pardir
        )
    )

    import apiai


# demo agent acess token: e5dc21cab6df451c866bf5efacb40178

CLIENT_ACCESS_TOKEN = 'cf9407017ab14315b24c0d92e29349cf'


def main():
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
    # open a file

    while True:
        print(u"user> ", end=u"")
        user_message = input()

        if user_message == u"exit":
            break
        if user_message==u"bye":
            "ThankYou"

        request =ai.text_request()
        request.query = user_message

        response = json.loads(request.getresponse().read())


        #Write the user query and bot response to a file
        result = response['result']
        # resolved query is to get the user response from the json data
        data= result.get('resolvedQuery')
        #speech is to get the bot response from the json data
        data1=response['result']['fulfillment']['speech']
        fo = open("D:/chatconv.txt", "a+")
        fo.write('user> '+data)
        fo.write('\n')
        fo.write('\n')
        fo.write('bot> '+data1)
        fo.write('\n')
        action = result.get('action')
        actionIncomplete = result.get('actionIncomplete', False)

        print(u"Bot> %s" % response['result']['fulfillment']['speech'])

        if action is not None:
            if action == u"send_message":
                parameters = result['parameters']

                text = parameters.get('text')
                message_type = parameters.get('message_type')
                parent = parameters.get('parent')

                print (
                    'text: %s, message_type: %s, parent: %s' %
                    (
                        text if text else "null",
                        message_type if message_type else "null",
                        parent if parent else "null"
                    )
                )

                if not actionIncomplete:
                    print(u"...Sending Message...")
                    break


if __name__ == '__main__':
    main()