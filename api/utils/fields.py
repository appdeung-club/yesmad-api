import hashlib
import random
import string

from mongoengine import StringField


class PasswordField(StringField):
    """A password field - generate password using specific algorithm (md5,sha1,sha512 etc) and regex validator

        Default regex validator: r[A-Za-z0-9] <- Match any of the above: leters and digits

        Example:

            class User(Document):
                username  = StringField(required=True,unique=True)
                password  = PasswordField(algorithm="md5")
                ip        = IPAddressField()

            # save user:
            user = User(username=username,password="mongoengine789",ip="192.167.12.255")
            user.save()

            # search user
            user = User.objects(username=username).first()
            if user is None:
                print "Not found!"
                return
            user_password = user.password
            print str(upassword) -> {'hash': 'c2e920e469d14f240d4de02883489750a1a63e68', 'salt': 'QBX6FZD', 'algorithm': 'sha1'}
            ... check password ...

    """
    ALGORITHM_MD5 = "md5"
    ALGORITHM_SHA1 = "sha1"
    ALGORITHM_SHA256 = "sha256"
    ALGORITHM_SHA512 = "sha512"
    DOLLAR = "$"

    def __init__(self, min_length=6,  max_length=None, salt=None,
                 algorithm=ALGORITHM_SHA1, **kwargs):
        self.max_length = max_length
        self.min_length = min_length
        self.algorithm = algorithm.lower()
        self.salt = salt or self.random_password()
        super(PasswordField, self).__init__(kwargs)

    def random_password(self, nchars=6):
        chars   = string.printable
        hash    = ''
        for char in range(nchars):
            rand_char = random.randrange(0, len(chars))
            hash += chars[rand_char]
        return hash

    def hexdigest(self, password):
        salted_password = str(self.salt + password).encode('utf-8')
        # use sha1 algoritm
        if self.algorithm == PasswordField.ALGORITHM_SHA1:
            return hashlib.sha1(salted_password).hexdigest()
        elif self.algorithm == PasswordField.ALGORITHM_MD5:
            return hashlib.md5(salted_password).hexdigest()
        elif self.algorithm == PasswordField.ALGORITHM_SHA256:
            return hashlib.sha256(salted_password).hexdigest()
        elif self.algorithm == PasswordField.ALGORITHM_SHA512:
            return hashlib.sha512(salted_password).hexdigest()
        raise ValueError('Unsupported hash type %s' % self.algorithm)

    def set_password(self, password):
        """
            Sets the user's password using format [encryption algorithm]$[salt]$[password]
                Example: sha1$SgwcbaH$20f16a1fa9af6fa40d59f78fd2c247f426950e46
        """
        password =  self.hexdigest(password)
        return '%s$%s$%s' % (self.algorithm, self.salt, password)

    def to_mongo(self, value):
        return self.set_password(value)

    def to_python(self, value):
        """
            Return password like sha1$DEnDMSj$ef5cd35779bba65528c900d248f3e939fb495c65
        """
        return value
