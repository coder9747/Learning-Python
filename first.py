# list = [1,2,3,4,5];
# list2 = [10,20,30,40,50,60,70,80,90,100];

# list+=list2
# print(list);

# days = ("sunday","monday","tuesday","firday","saturday");

# list2 = list(days);

# list2.insert("thursday",3);

# days = tuple(list2);

# print(days);

# myDist = {
#     "name":"pratyush",
#     "age":22,

# }


# def sum(x,y):
#     return x + y;



# def swap(list,s,e):
#     temp = list[s];
#     list[s] = list[e];
#     list[e] = temp;


# list = [1,2,3,4,5,6,7,7,8,10];
# s = int(0);
# e = int(len(list)-1);
# while(s<=e):
#     swap(list,s,e);
#     s+=1;
#     e-=1;
    

# print(list);

# name = input("Enter Your Name");


# print("Your Name is {}".format(name));


# list = [];
# for i in range(101):
#     list.append(i);


# print(list);
# s = 0;
# e = len(list)-1;
# while(s<e):
#     temp = list[s];
#     list[s] = list[e];
#     list[e] = temp;

# print(list);

# list = [1,2,1,2,4,4,5];

# x = 0;


# xor = 0;


# for i in list:
#     xor = xor ^ i;


# print(list);
# def swap(list,s,e):
#     temp = list[s];
#     list[s] = list[e];
#     list[e] = temp;


# list = [0,0,3,0,0,45,0,0,56,77];
# s = 0;
# e = 0;
# while e<len(list):
#     if(list[e]!=0):
#         swap(list,s,e);
#         s+=1;
#     e+=1;


# print(list);


a = 15;
b = 10;

print("a:{} b:{}".format(a,b));

a^=b;
b^=a;
a^=b;

print("a:{} b:{}".format(a,b));