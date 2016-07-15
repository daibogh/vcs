import os
import pickle
import variables as var
def create_necessary_files():
    os.chdir(var.administration)
    base_struct = {}
    f1 = open('users_requests.txt','wb')
    f2 = open('users_rights_for_projects.txt','wb')
    pickle.dump(base_struct, f1)
    pickle.dump(base_struct, f2)
    f1.close()
    f2.close()