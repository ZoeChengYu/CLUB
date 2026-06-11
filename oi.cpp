#include <iostream>

int u=0;
int main();

int outoma(int k){
    std::cout<<"out"<<k<<std::endl;
    u=k<<1;
    main();
    
    return k;
}

int infoma(int g){
    std::cout<<"in"<<g<<std::endl;
    g*=-1;
    outoma(g);
    
    return 0;
}

int main()
{
    std::cout<<"main"<<u<<std::endl;
    u+=1;
    infoma(u);
    
    return 0;
}