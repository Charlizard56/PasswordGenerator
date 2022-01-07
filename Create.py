import Gen
import List_and_tuples



def create(times_,t_,symbol_,number_,letters_lower_,letters_upper_):

    while True:
        Gen.gen(times_, t_)
        print(List_and_tuples.Password_Gen)
        t_ = Gen.Check(symbol_, number_, letters_lower_, letters_upper_)
        if t_:
            print("All True")
            # Crate String For Password
            List_and_tuples.Password = ""
            for p_g in List_and_tuples.Password_Gen:
                List_and_tuples.Password += p_g
                print(List_and_tuples.Password)
            return List_and_tuples.Password
        else:
            print("Continue")
            List_and_tuples.Password_Gen = []
            continue
