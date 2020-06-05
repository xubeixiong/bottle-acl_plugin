+ ### bottle-aclPlugin

---

A plug-in for permission control. User permission is defined by himself



## Usage

~~~text
pip install bottle-aclPlugin==0.1.0
~~~

or

~~~text
python3 -m pip install bottle-aclPlugin
~~~



you must create an object and inherit  **AclPlugin** and Implement  ***get_roles***.

~~~python
from bottle-aclPlugin import AclPlugin
class AclSonPlugin(AclPlugin):

    def get_roles(self, arg):
        # get user's roles in arg
        
        return {roles}
~~~



install plugin objects at the beginning.

~~~python
import bottle
import AclSonPlugin

app = bottle.default_app()

acl = app.install(AclSonPlugin())
~~~



Then you can use the **Plugin** carry out authority control for designated api.

~~~python
import acl

@app.get("/Admin")
@acl.roles_required(roles={"admin"})
def get_admin():
    return "okmsg"
~~~



