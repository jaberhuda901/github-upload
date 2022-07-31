
from math import sqrt  


owsj_length = 2.5
truss_debth = 3.5
hyptonus = 18.5

weight_2_5 = 0
weight_3_5 = 0 
weight_hyp = 0 



reaction = -583.5375 
p_f = 89.775 

'''
the following python script is used to calculate the internal forces of all the members. The T after each force value refers to that member is in tension.  
The C after each force value refers to that member is in Compression. For Example: AP  ->  717.111340073841 T , the following member AP is in Tension and has a force of 717.111340073841 kN 
The force value associated with eachmember is in kiloNewtons. 

The script takes all the vertical forces acting on Joint as zero and then calculates the missing forces of the Joint.   
The script also takes all the Horizontal forces acting on Joint as zero and then calculates the missing forces of the Joint. 

'''

############################## Calculation of Force Members AP,AB,BP,BC,PC,PQ ################################

lst_force_values_L = []
lst_members_L = ['AP','AB','BP','BC','PC','PQ' ] 

force_AP = (sqrt(hyptonus)/truss_debth) * (reaction + weight_2_5 + weight_hyp )    # takes all the vertical forces acting on Joint A 
force_AP = abs(force_AP)
lst_force_values_L +=  [force_AP]

force_AB = -((owsj_length/sqrt(hyptonus)) * force_AP)   # takes all the Horizontal forces acting on Joint A 
force_AB = abs(force_AB)
lst_force_values_L +=  [force_AB] 

force_BP = 89.775 + weight_2_5 + weight_2_5 + weight_3_5      # takes all the vertical forces acting on Joint B But as the member BP only applies the vertical force in joint B. Therefore, force_BP = 89.775        
lst_force_values_L +=  [force_BP]

place_holder = force_AB                     # takes all the Horizontal forces acting on Joint B But as the member AB and BC only applies the Horizontal force in joint B. Therefore, force_BC = force_AB 
force_BC = place_holder 
lst_force_values_L +=  [force_BC] 

force_PC =  (((-1*(truss_debth/sqrt(hyptonus))) * 717.1113) + (89.775 + weight_2_5 + weight_hyp + weight_hyp + weight_3_5 )) / (truss_debth/sqrt(hyptonus)) # takes all the vertical forces acting on Joint P
    
force_PC = abs(force_PC)
lst_force_values_L +=  [force_PC]

force_PQ = ((owsj_length/sqrt(hyptonus))*force_AP) +  ((owsj_length/sqrt(hyptonus))*force_PC)  # takes all the Horizontal forces acting on Joint P 
lst_force_values_L +=  [force_PQ]  




############################## Calculation of Force Members 2O,ON,2N,NM,2M,21 ################################

lst_force_values_R = []
lst_members_R = ['2O','ON','2N','NM','2M','21' ] 

force_O2 = (sqrt(hyptonus)/truss_debth) * (reaction + weight_2_5 + weight_hyp )    # takes all the vertical forces acting on Joint O 
force_O2 = abs(force_O2) 
lst_force_values_R +=  [force_O2] 

force_ON = -((owsj_length/sqrt(hyptonus)) * force_O2)    # takes all the Horizontal forces acting on Joint O
force_ON = abs(force_ON)  
lst_force_values_R +=  [force_ON]

force_N2 = 89.775 + weight_2_5 + weight_2_5 + weight_3_5                            # takes all the vertical forces acting on Joint N But as the member 2N only applies the vertical force in joint N. Therefore, force_N2 = 89.775 
lst_force_values_R +=  [force_N2]

place_holder = force_AB                      # takes all the Horizontal forces acting on Joint N But as the member MN and ON only applies the Horizontal force in joint N. Therefore, force_NM = force_AB = force_ON
force_NM = place_holder 
lst_force_values_R +=  [force_NM]

force_M2 =  (((-1*(truss_debth/sqrt(hyptonus))) * 717.1113) + (89.775 + weight_2_5 + weight_hyp + weight_hyp + weight_3_5 )) / (truss_debth/sqrt(hyptonus))      # takes all the vertical forces acting on Joint 2
force_M2 = abs(force_M2)
lst_force_values_R +=  [force_M2]

force_12 = ((owsj_length/sqrt(hyptonus))*force_O2) +  ((owsj_length/sqrt(hyptonus))*force_M2)             # takes all the Horizontal forces acting on Joint 2 
lst_force_values_R +=  [force_12] 




############ Calculation of Force Members CQ,CD,QD,QR,RD,DE,RE,RS,SE,EF,SF,ST,TF,FG,TG,TU,UG,GH,UH,UV #############

#  The code from line 81 to 133 is use to Calculation the Force in Members CQ,CD,QD,QR,RD,DE,RE,RS,SE,EF,SF,ST,TF,FG,TG,TU,UG,GH,UH,UV. 



i = 0 

input_top_h = place_holder  
input_top_s = force_PC
input_bottom_h = force_PQ

lst_force_values = []
lst_members_l_to_r = ['CQ','CD','QD','QR','RD','DE','RE','RS','SE','EF','SF','ST','TF','FG','TG','TU','UG','GH','UH','UV' ] 

while i < 5 : 
    
    
    
    #### Calculation of all the Joints above Joint Q #######
    
    
    ## sum of vertical forces of joint ##
    
    force_DR = (89.775 + weight_2_5 + weight_2_5 + weight_hyp + weight_3_5 ) - ((truss_debth/sqrt(hyptonus)) * input_top_s)   
    lst_force_values +=  [force_DR]
    #print(force_DR)
    
    
    ## sum of Horizontal forces of joint ##
    
    force_DE = (-(owsj_length/sqrt(hyptonus)) * input_top_s) - input_top_h 
    lst_force_values +=  [force_DE]
    #print(force_DE)
    
    
    
    #print('') 
    
    
    
    #### Calculation of all the Joints bellow Joint C #######
    
    ## sum of vertical forces of joint ##
    
    force_RE = (sqrt(hyptonus)/truss_debth) * ( (-1 * abs(force_DR)) - weight_2_5 - weight_2_5 - weight_3_5 - weight_hyp  )  
    lst_force_values +=  [force_RE]
    #print(force_RE)    
    
    ## sum of Horizontal forces of joint  ##
    
    force_RS = ((owsj_length/sqrt(hyptonus)) * abs(force_RE)) + abs(input_bottom_h) 
    lst_force_values +=  [force_RS]
    #print(force_RS)
    
    
    #print('')
        
    ##### CHANGING INITIAL 
    
    input_top_h = abs(force_DE) 
    input_top_s = abs(force_RE)
    input_bottom_h = abs(force_RS)    
    
    
    i += 1

lst_T_and_C = 5 * ['T','C','C','T']




####################### MAIN Print ###########################################

# the "MAIN Print" prints the values obtained  

print('')

lst_T_and_C_1 = ['T','C','C','C','C','T']
    
y = 0
while y < 6:
    #print(y)
    print(lst_members_L[y] +'  ->  '+ str((lst_force_values_L[y])) +' '+ lst_T_and_C_1[y]  ) 
    y += 1


y = 0
while y < 20:
    #print(y)
    print(lst_members_l_to_r[y] +'  ->  '+ str(abs(lst_force_values[y])) +' '+ lst_T_and_C[y]  ) 
    y += 1 




    
####################### MAIN Print ###########################################
    
    
    

############ Calculation of Force Members M1,ML,QD,1L,ZL,LK,ZK,ZY,YK,KJ,YJ,YX,XJ,JI,XI,XW,WI,IH,WH,WV #############

#  The code from line 170 to 233 is use to Calculation the Force in Members M1,ML,QD,1L,ZL,LK,ZK,ZY,YK,KJ,YJ,YX,XJ,JI,XI,XW,WI,IH,WH,WV. 

i = 0 
    
input_top_h = 416.8125 
input_top_s = 606.7865
input_bottom_h = 769.5000
    
lst_force_values = []
lst_members_r_to_l = ['M1','ML','QD','1L','ZL','LK','ZK','ZY','YK','KJ','YJ','YX','XJ','JI','XI','XW','WI','IH','WH','WV' ] 
    
while i < 5 : 
        
        
        
        #### Calculation of all the Joints above Joint 1 #######
        
        
        ## sum of vertical forces of joint ##
        
    force_DR = (89.775 + weight_2_5 + weight_2_5 + weight_hyp + weight_3_5 ) - ((truss_debth/sqrt(hyptonus)) * input_top_s)   
    lst_force_values +=  [force_DR]
        #print(force_DR)
        
        
        ##  sum of Horizontal forces of joint  ##
        
    force_DE = (-(owsj_length/sqrt(hyptonus)) * input_top_s) - input_top_h 
    lst_force_values +=  [force_DE]
        #print(force_DE)
        
        
        
        #print('') 
        
        
        
        #### Calculation of all the Joints bellow Joint M #######
        
        ## sum of vertical forces of joint ##
        
    force_RE = (sqrt(hyptonus)/truss_debth) * ( (-1 * abs(force_DR)) - weight_2_5 - weight_2_5 - weight_3_5 - weight_hyp  )  
    lst_force_values +=  [force_RE]
        #print(force_RE)    
        
        ##  sum of Horizontal forces of joint  ##
        
    force_RS = ((owsj_length/sqrt(hyptonus)) * abs(force_RE)) + abs(input_bottom_h) 
    lst_force_values +=  [force_RS]
        #print(force_RS)
        
        
        #print('')
            
        ##### CHANGING INITIAL 
        
    input_top_h = abs(force_DE) 
    input_top_s = abs(force_RE)
    input_bottom_h = abs(force_RS)    
        
        
    i += 1
    
lst_T_and_C = 5 * ['T','C','C','T']
    
        
#print(len(lst_force_values))
    #print(len(lst_T_and_C))
    
 

############################ Calculation of Force in Member HV #############################
    
force_HV = 89.775 - ((truss_debth/sqrt(hyptonus))* abs(lst_force_values[18])) - ((truss_debth/sqrt(hyptonus))* abs(lst_force_values[18]))
force_HV = int(force_HV)
#print('HV  -> ',force_HV)
print('')

####################### MAIN Print 2 ###########################################

# the "MAIN Print 2" prints the values obtained 
   
y = 0
while y < 20:
    #print(y)
    print(lst_members_r_to_l[19-y] +'  ->  '+ str(abs(lst_force_values[19-y])) +' '+ lst_T_and_C[3-y]  ) 
    y += 1
    

    
lst_T_and_C_1 = ['T','C','C','C','C','T']
        
y = 0
while y < 6:
    #print(y)
    print(lst_members_R[5-y] +'  ->  '+ str((lst_force_values_R[5-y])) +' '+ lst_T_and_C_1[5-y]  ) 
    y += 1
print('')