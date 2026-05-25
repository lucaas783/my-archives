int main(void){

    char mapa[20][40];
    int i, j;
    for(i = 0; i < 20; i++){
        for(j = 0; j < 40; j++){
            if(i == 0 || i == 19 || j == 0 || j == 39){
                mapa[i][j] = '#';
            } else {
                mapa[i][j] = ' ';
            }
        }
    }
}