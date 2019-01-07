import pandas as pd
import numpy as np
import pickle
import mathematical_formulation_robust as cn


            

            




class informs:
    def __init__(self,omega_multi,alpha_multi,w_pre,O_scale,dic_sector,dic_bench,risk_sedol,dic_MCAP,dic_beta,alpha,risk_mat,pie_scale,alpha_b,lamda):


        self.dic_sector = dic_sector
        self.dic_bench = dic_bench
        self.risk_sedol = risk_sedol
        self.dic_MCAP = dic_MCAP
        self.dic_beta = dic_beta
        self.alpha = alpha
        self.risk_mat = risk_mat
        self.omegamulti = omega_multi
        self.conlist = [0,1,2,3,4,5]
        self.w_pre = w_pre
        lamda = lamda
        q_con1 = []
        q_con2 = []
        q_val = []
        
        for i in range(len(self.alpha)):
            self.alpha[i] = self.alpha[i]*alpha_multi

        for i in range(len((self.risk_mat[0]))):
            for j in range(len(self.risk_mat[0])):
                if j >= i:
                    q_con1.append(i)
                    q_con2.append(j)
                    if i == j:
                        ex_list = list(self.risk_mat[i])
                        q_val.append(omega_multi * ex_list[j])
                    else:
                        ex_list = list(self.risk_mat[i])
                        q_val.append(2*omega_multi * ex_list[j])

        Q_cons = []
        Q_cons.append(q_con1)
        Q_cons.append(q_con2)
        Q_cons.append(q_val)
        self.Q_con = Q_cons

        self.cplexs = cn.portfolio(sector=self.dic_sector, bench=self.dic_bench, asset=self.risk_sedol, MCAPQ=self.dic_MCAP, beta=self.dic_beta,alpha=self.alpha,w_pre=w_pre,O_scale=O_scale,pie_scale=pie_scale,lamda=lamda,alpha_b=alpha_b)



        
     
        
        
        
    def set_omega(self,risk_mat):
      #  print("ome시작")

        self.qmat = []

        sedol_var_list = []

        for i in self.risk_sedol:
            sedol_var_list.append("d" + str(i))



        sedol_var_list.append("assum")
        
        sedol_var_list.append("O")
        
        for i in self.w_pre.keys():
            sedol_var_list.append("dx" + str(i))
            
        sedol_var_list.append("pie")
        
        for i in self.risk_sedol:
            sedol_var_list.append("seta" + str(i))
            
        for i in self.risk_sedol:
            sedol_var_list.append("p" + str(i))
        

        for i in range(len(risk_mat)):
            qmat_1 = []
            qmat_1.append(sedol_var_list)
            new_risk_mat = []
            for j in risk_mat[i]:
                new_risk_mat.append(2*j*self.omegamulti)
            new_risk_mat.append(0)
            new_risk_mat.append(0)
            for j in self.w_pre.keys():
                new_risk_mat.append(0)
            new_risk_mat.append(0)
            for j in risk_mat[i]:
                new_risk_mat.append(0)
            for j in risk_mat[i]:
                new_risk_mat.append(0)
            qmat_1.append(new_risk_mat)
            self.qmat.append(qmat_1)

        for i in range(2):
            qmat_1 = []
            qmat_1.append(sedol_var_list)
            new_risk_mat = []
            for j in range(len(risk_mat[0])):
                new_risk_mat.append(0)
            new_risk_mat.append(0)
            new_risk_mat.append(0)
            for j in self.w_pre.keys():
                new_risk_mat.append(0)
            new_risk_mat.append(0)
            for j in risk_mat[i]:
                new_risk_mat.append(0)
            for j in risk_mat[i]:
                new_risk_mat.append(0)
            qmat_1.append(new_risk_mat)
            self.qmat.append(qmat_1)
            
        for i in range(len(self.w_pre.keys())):
            qmat_1 = []
            qmat_1.append(sedol_var_list)
            new_risk_mat = []
            for j in range(len(risk_mat[0])):
                new_risk_mat.append(0)
            new_risk_mat.append(0)
            new_risk_mat.append(0)
            for j in self.w_pre.keys():
                new_risk_mat.append(0)
            new_risk_mat.append(0)
            for j in risk_mat[0]:
                new_risk_mat.append(0)
            for j in risk_mat[0]:
                new_risk_mat.append(0)
            qmat_1.append(new_risk_mat)
            self.qmat.append(qmat_1)
            
            
            
        for i in range(1):
            qmat_1 = []
            qmat_1.append(sedol_var_list)
            new_risk_mat = []
            for j in range(len(risk_mat[0])):
                new_risk_mat.append(0)
            new_risk_mat.append(0)
            new_risk_mat.append(0)
            for j in self.w_pre.keys():
                new_risk_mat.append(0)
            new_risk_mat.append(0)
            for j in risk_mat[i]:
                new_risk_mat.append(0)
            for j in risk_mat[i]:
                new_risk_mat.append(0)
            qmat_1.append(new_risk_mat)
            self.qmat.append(qmat_1)
            
        for i in range(len(risk_mat)):
            qmat_1 = []
            qmat_1.append(sedol_var_list)
            new_risk_mat = []
            for j in range(len(risk_mat[0])):
                new_risk_mat.append(0)
            new_risk_mat.append(0)
            new_risk_mat.append(0)
            for j in self.w_pre.keys():
                new_risk_mat.append(0)
            new_risk_mat.append(0)
            for j in risk_mat[i]:
                new_risk_mat.append(0)
            for j in risk_mat[i]:
                new_risk_mat.append(0)
            qmat_1.append(new_risk_mat)
            self.qmat.append(qmat_1)
            
            
            
        for i in range(len(risk_mat)):
            qmat_1 = []
            qmat_1.append(sedol_var_list)
            new_risk_mat = []
            for j in range(len(risk_mat[0])):
                new_risk_mat.append(0)
            new_risk_mat.append(0)
            new_risk_mat.append(0)
            for j in self.w_pre.keys():
                new_risk_mat.append(0)
            new_risk_mat.append(0)
            for j in risk_mat[i]:
                new_risk_mat.append(0)
            for j in risk_mat[i]:
                new_risk_mat.append(0)
            qmat_1.append(new_risk_mat)
            self.qmat.append(qmat_1)
            
            
        

        a = np.full((len(self.alpha), len(self.alpha)), self.omegamulti)

        self.risk_mat = risk_mat * a
        self.cplexs.quard_con(Q_con=self.Q_con,multiple=self.omegamulti)
        self.cplexs.quard_obj(qmat=self.qmat)



    def set_con(self,cons):

        self.conlist = cons
        self.cplexs.set_con(sols=self.conlist)


    def solve(self,end_cond):
        

        mins_list = []
        mins_list2 = []


        rss = []

        self.returns = 0

        w_up_dic = {}

        for i in self.risk_sedol:
            w_up_dic.update({i: 0})
                   
        self.cplexs.set_upsum(big_w_dic=w_up_dic, w_upsums=0)                                                                              
        
        list_result = self.cplexs.solves()
        
        
        if list_result == 1234:
            
            return 1234
            
        

        w_dic = list_result[0]
        d_dic = list_result[1]
        rs = list_result[2]
        rss.append(rs)
        sum_min = 0
        mat_1 = np.empty(shape=[0, len(self.alpha)])
        mat_2 = np.zeros((len(self.risk_sedol), 1))
        

        for i in w_dic.keys():
            
            sum_min += min(w_dic[i], self.dic_bench[i])


        mins_list.append(1 - sum_min)

        active_share = 1 - sum_min

        print("AC")
        print(active_share)
        
        
        DP = 1.0/float(len(self.conlist))

        k = 0

        for i in self.risk_sedol:
            mat_1 = np.append(mat_1, d_dic[i])
            mat_2[k] = np.array([d_dic[i]])
            k += 1



        a = np.dot(mat_1, self.risk_mat)
        b = np.dot(a, mat_2)
        c = np.dot(mat_1,a)
        acnum = 0
        
        print("TE")
        
        print(b)
        mins_list2.append(b)

        TE = b

        w_upsum = 0
        
        TE_S = 1000
        TE_out = 0
        TE_ch = 9999
        nnn = 0
        
        
        for i in self.risk_sedol:
            if w_dic[i] > 0:
                if TE_ch > abs((w_dic[i]-self.dic_bench[i])*(w_dic[i]-self.dic_bench[i])*self.risk_mat[nnn][nnn]):
                    TE_ch = abs((w_dic[i]-self.dic_bench[i])*(w_dic[i]-self.dic_bench[i])*self.risk_mat[nnn][nnn])
                    TE_out = nnn
            
            nnn += 1
        
        
        if list_result[4] != 1:
            
            print("infeasible")

            non_fea = 0
            in_se = 0
            out_se = 0
            in_Mc = 0
            out_Mc = 0

            # (6)
            dic_se = {}
            dic_se2 = {}
            for i in self.dic_sector:
                
                chek_sect = 0
                for j in self.dic_sector[i]:
                    chek_sect += w_dic[j]-self.dic_bench[j]
                dic_se.update({i:chek_sect})
                dic_se2.update({i:abs(chek_sect)})
            for i in dic_se:
                if abs(dic_se[i]) > 0.1:
                    non_fea = 1
                    if dic_se[i] > 0.1:
                        out_se = i
                        in_se = min(dic_se2.keys(), key=(lambda k: dic_se2[k]))
                    if dic_se[i] < -0.1:
                        out_se =  min(dic_se2.keys(), key=(lambda k: dic_se2[k]))
                        in_se = i
                    print("st_6 infeasible and infeasible sector is : ",i)
                    return "sector",in_se,out_se
                    

            # (7)
            dic_M = {}
            dic_M2 = {}
            for i in self.dic_MCAP:
                chek_mcap = 0
                for j in self.dic_MCAP[i]:
                    chek_mcap += w_dic[j]-self.dic_bench[j]
                dic_se.update({i:chek_mcap})
                dic_se2.update({i:abs(chek_mcap)})
            for i in dic_M:
                if abs(dic_M[i]) > 0.1:
                    non_fea = 1
                    if dic_M[i] > 0.1:
                        in_Mc = min(dic_M2.keys(), key=(lambda k: dic_M2[k]))
                        out_Mc = i
                    if dic_M[i] < -0.1:
                        out_Mc = min(dic_M2.keys(), key=(lambda k: dic_M2[k]))
                        in_Mc = i
                    print("st_7 infeasible and infeasible mcapq is : ",i)
                    return "MCAPQ",in_Mc,out_Mc
            

            # (8)
            chek_beta = 0
            for i in self.risk_sedol:
                chek_beta += (w_dic[i]-self.dic_bench[i])*self.dic_beta[i]
        
            if abs(chek_beta) > 0.1:
                non_fea = 1
                print("st_8 infeasible")
                return 0,TE_out
            
            
            if non_fea == 0:
                return 0,TE_out 
        

            
        wupchek = 0
        wsum = 0
        

        for i in w_dic.keys():
            wsum += w_dic[i]

            if w_dic[i] < DP:
                w_up_dic.update({i: 1})
                w_upsum += w_dic[i]
                wupchek += 1

        end = False

        if active_share >= 0.6 and TE >= 0.0025*self.omegamulti:
            
            return list_result,TE_out
            end = False
        else:
            end = True
            


            
            
        if active_share < 0.6:
            acnum += 1
            
        dist = 1
        w_upsum2 = 1.0 
        Feasible_check = 0
        final_result_dic = []
        


        while (end):
            if dist < end_cond:
      
                if len(final_result_dic) == 0:

                    return 0,TE_out

                else:

                    return final_result_dic,TE_out

                break

            w_upsum_in = (w_upsum + w_upsum2) * 0.5
            self.cplexs.set_upsum(big_w_dic=w_up_dic, w_upsums=w_upsum_in)
            
            try:
                list_result2 = self.cplexs.solves()
            except:

                return 0,TE_out
                break
                


            w_dic = list_result2[0]
            d_dic = list_result2[1]
            rs = list_result2[2]
            sum_min = 0
            mat_1 = np.empty(shape=[0, len(self.alpha)])
            mat_2 = np.zeros((len(self.risk_sedol), 1))

            for i in w_dic.keys():
                sum_min += min(w_dic[i], self.dic_bench[i])

            active_share = 1 - sum_min

            k = 0

            for i in self.risk_sedol:
                mat_1 = np.append(mat_1, d_dic[i])
                mat_2[k] = np.array([d_dic[i]])
                k += 1

            a = np.dot(mat_1, self.risk_mat)
            b = np.dot(a, mat_2)
            TE = b



            
            if active_share < 0.6:
                acnum += 1
            if active_share < 0.6 or TE < 0.0025*self.omegamulti:
                dist = w_upsum2 - w_upsum_in
                w_upsum = w_upsum_in
            elif list_result2[4] != 1 and len(final_result_dic) == 0:

                non_fea = 0
                in_se = 0
                out_se = 0
                in_Mc = 0
                out_Mc = 0

                # (6)
                dic_se = {}
                dic_se2 = {}
                for i in self.dic_sector:

                    chek_sect = 0
                    for j in self.dic_sector[i]:
                        chek_sect += w_dic[j]-self.dic_bench[j]
                    dic_se.update({i:chek_sect})
                    dic_se2.update({i:abs(chek_sect)})
                for i in dic_se:
                    if abs(dic_se[i]) > 0.1:
                        non_fea = 1
                        if dic_se[i] > 0.1:
                            out_se = i
                            in_se = min(dic_se2.keys(), key=(lambda k: dic_se2[k]))
                        if dic_se[i] < -0.1:
                            out_se =  min(dic_se2.keys(), key=(lambda k: dic_se2[k]))
                            in_se = i

                        return "sector",in_se,out_se


                # (7)
                dic_M = {}
                dic_M2 = {}
                for i in self.dic_MCAP:
                    chek_mcap = 0
                    for j in self.dic_MCAP[i]:
                        chek_mcap += w_dic[j]-self.dic_bench[j]
                    dic_se.update({i:chek_mcap})
                    dic_se2.update({i:abs(chek_mcap)})
                for i in dic_M:
                    if abs(dic_M[i]) > 0.1:
                        non_fea = 1
                        if dic_M[i] > 0.1:
                            in_Mc = min(dic_M2.keys(), key=(lambda k: dic_M2[k]))
                            out_Mc = i
                        if dic_M[i] < -0.1:
                            out_Mc = min(dic_M2.keys(), key=(lambda k: dic_M2[k]))
                            in_Mc = i

                        return "MCAPQ",in_Mc,out_Mc
                        



                
                
                
                dist = w_upsum_in - w_upsum
                w_upsum2 = w_upsum_in

            
            else:
                dist = w_upsum_in - w_upsum
                w_upsum2 = w_upsum_in
                Feasible_check += 1              
                if Feasible_check == 1:
                    final_result_dic = list_result2
                    chobj = list_result2[2]
                if Feasible_check > 1:
                    if chobj > list_result2[2]:
                        final_result_dic = list_result2
                        chobj = list_result2[2]
                
