<h1>Installing</h1>

You can install PaymeAPI using pip:

<pre lang="bash">
pip install PaymeAPI
</pre>


<h1>Usage</h1>

To use PaymeAPI, first import the <code>PaymeAPI</code> class from the <code>payme</code> package:

<pre lang="python">
# Import lib
from payme import Payme
# Create a client instance with your card ID
client = Payme(mycard=' ')

# Call the create method to create a payment
response = client.create(summ=10000, desc='Test Payment')

check_id = response['result']['id']
check_out = response['result']['pay_url']

# Call the info method to get the payment status
status = client.info(check_id=check_id)
</pre>


<h1>License</h1>
PaymeAPI is licensed under the MIT License.