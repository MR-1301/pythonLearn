# Method-1
import ecommerce.shipping

ecommerce.shipping.calc_shipping()
ecommerce.shipping.calc_tax()

# Method-2: importing required functions from modules
from ecommerce.shipping import calc_shipping, calc_tax

calc_shipping()
calc_tax()

# Method-3: improting entire module
from ecommerce import shipping

shipping.calc_shipping()
shipping.calc_tax()
