import os


"""
    Here the idea is to build any class or function to help me
    handle the diff request that come thru all the webhooks
"""


class BaseVerification():
    """This class is intended to handle the 
    verification sent from meta, annd be reusable for
    every webhook"""
    
    def __init__(self, request):
        self.request = request
    
    def verify_token(self):
        """This method verfy each token for every
        webhook suscribed
        """

        if self.request.method == 'GET':
            # Here I need the logic to select the token
            token = os.environ.get('VERIFY_TOKEN')
            if self.request.GET.get('hub.verify_token') == token:
                return {
                'hub.challenge':self.request.GET.get('hub.challenge'),
                'status': 200
                }
            else: return {'hub.challenge':'','status': 403}
        
        return None