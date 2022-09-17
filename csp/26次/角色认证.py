"""Author = GARKAX GY
Date: 2022--12
TIME FLIES!
"""


def main():
    usr_lst = {}
    grp_lst = {}
    role_dst = {}
    n, m, q = map(int, input().split())
    for x in range(n):
        role_msg = input().split()
        status = role_msg.pop(0)
        new_role = role_dst[status] = Role(status)
        for j in range(int(role_msg.pop(0))):
            new_role.append_op(role_msg.pop(0))
        for j in range(int(role_msg.pop(0))):
            new_role.append_src(role_msg.pop(0))
        for j in range(int(role_msg.pop(0))):
            new_role.append_src_name(role_msg.pop(0))

    for x in range(m):
        usr_msg = input().split()
        role, num_usr, typ = usr_msg[0], int(usr_msg[1]), usr_msg[2]
        if typ == "u":
            for j in range(num_usr):
                name = usr_msg.pop()
                new_usr = Usr(name, role)
                usr_lst[name] = new_usr
        else:
            for j in range(num_usr):
                name = usr_msg.pop()
                new_usr = Grp(name, role)
                grp_lst[name] = new_usr

    for x in range(q):
        usr, num_grp, name_grp, name_op, tpy_src, name_src = map(str, input().split())
        test_msg = input().split()
        usr_name, grp_num = test_msg.pop(0), int(test_msg.pop(0))
        tmp_role = []
        for i in range(grp_num):
            grp_name = test_msg.pop(0)
            tmp_role.append(grp_lst[grp_name].get_role()) if grp_name in grp_lst else 0
        if usr_name in usr_lst:
            tmp_role.append(usr_lst[usr_name].get_role())
        for role in tmp_role:
            return 1 if role.if_operate() and role.if_src() else 0


class Role(object):
    def __init__(self, name):
        self.__name = name
        self.__operator = []
        self.__source = []
        self.__nameOfSrc = []

    def if_operate(self, op):
        return True if op in self.__operator else False

    def if_src(self, src):
        return True if src in self.__source else False

    def if_name(self, name):
        return True if name in self.__nameOfSrc else False

    def append_op(self, op):
        self.__operator.append(op)

    def append_src(self, src):
        self.__source.append(src)

    def append_src_name(self, name):
        self.__nameOfSrc.append(name)



class Usr(object):
    def __init__(self, name, role):
        self.__name = name
        self.__role = role
        self.__grp = []

    def ad_grp(self, grp):
        self.__grp.append(grp)

    def get_grp(self):
        return self.__grp

    def get_role(self):
        return self.__role

    def get_name(self):
        return self.__name


class Grp(object):
    def __init__(self, name, role):
        self.__name = name
        self.__role = role
        self.__member = []

    def ad_members(self, usr):
        self.__member.append(usr)

    def get_role(self):
        return self.__role
