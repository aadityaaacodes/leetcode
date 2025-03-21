
#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

bool inputCheck (char board[][3], int, int);
void nextMove(char[][3], int&, int&, char);
bool checkWin(char[][3]);
bool checkTie(char[][3]);
void printBoard(char[][3]);

int main()
{
    char keepPlaying;

    do              //The do-while loop continues until the player does not want to play anymore.
    {
        char board[3][3]={{'-','-','-'},{'-','-','-'},{'-','-','-'}};
        bool first_play = true; //Teach computer to occupy the center
        bool player_1_win, player_2_win, player_tie, player_1_illegal_input, player_2_illegal_input;
        player_1_win = false;
        player_2_win = false;
        player_tie = false;
        player_1_illegal_input = false;
        player_2_illegal_input = false;
        int play_count = 0;


        while(true)      //This while loop continues until the player or computer wins or there is tie.
        {
            int rowX=0, colX=0, rowO, colO, repeat;

            //player 1 starts here and player 1 is the computer
            nextMove(board, rowX, colX, 'X');
            if (!inputCheck (board, rowX, colX)){
                cout << "player-1 illegal input position \n";
                player_1_illegal_input = true;
                break;

            }
            board[rowX][colX]='X';   //this puts the X in the correct spot.
            cout << "Board content after player-1 plays" << endl;
            printBoard(board);  //This calls the printBoard function using call by value.
            play_count ++;

            if (checkWin(board)) //The if statement checks if the computer won and breaks out
               {
                  cout << "player-1 wins \n ";
                  player_1_win = true;
                  break;
               };
            if (checkTie(board))
               {
                  cout << "There is a tie \n";
                  player_tie = true;
                  break;
               };


                //Player 2 starts here and the human player (it is YOU) is Player 2
                //However, in unit testing, Player 2 is a smarter version called (nextMove_2())  with knowledge 

                cout << "what is your row? ";
                cin >> rowO;

                cout << "what is your column? ";
                cin >> colO;

                if (!inputCheck (board, rowO, colO)){
                    cout << "player-2 illegal input position \n";
                    player_2_illegal_input = true;
                    break;
                }

                board[rowO][colO]='O';    //This places an O in the correct stop.
                cout << endl;
                cout << "Board content after player-2 plays" << endl;
                printBoard(board);        //This prints the board again.
                if (checkWin(board)){
                  cout << "Player-2 win " << endl; //This checks if the player has won
                  player_2_win = true;
                  break;
                };
                if (checkTie(board)){
                   cout << "There is a tie " << endl;
                   player_tie = true;
                   break;
                }
            //} //end of user play
        } //end of while(true)

        cout << "play count for player 1 = " << play_count << endl;

        cout << "Do you want to play again? (Y/N)?" << endl;;
        cin >> keepPlaying;
    } while(keepPlaying=='Y');
    return 0;
}


bool inputCheck (char board[][3], int i, int j){

    //cout << "Print board inside input check" << endl;
    //printBoard(board);
    if (board[i][j]=='X')
        {

            cout << "That spot is already taken. Please choose another row and column."
                     << endl;
            return false;
        }
    else if (board[i][j]=='O')
        {

            cout << "That spot is already taken. Please choose another row and column."
                     << endl;
            return false;
        }
    else if (i>2||j>2||i<0||j<0)
        {
            cout << "You must choose either 0, 1, or 2. Please enter another row and column."
                    << endl;
            return false;
        }
    else
        return true;
}

void nextMove (char board[][3], int &row, int &col, char myToken)
{
    int repeat=1;
    while(repeat==1)
    {
        srand(time(0));
        row=rand()%3;
        col=rand()%3;
        if (board[row][col]=='X')
            repeat=1;
        else if (board[row][col]=='O')
            repeat=1;
        else
            repeat=0;
    }

}



//The following function check whether there is a winning board
bool checkWin(char board[][3])
{
  bool win = false;
  for (int i = 0; i <= 2; i++)
  {

      if (board[i][0] == 'X' && board[i][1] == 'X' && board[i][2] == 'X')  win = true; else
      if (board[i][0] == 'O' && board[i][1] == 'O' && board[i][2] == 'O')  win = true; else

      if (board[0][i] == 'X' && board[1][i] == 'X' && board[2][i] == 'X')  win = true; else
      if (board[0][i] == 'O' && board[1][i] == 'O' && board[2][i] == 'O')  win = true;
   }

   if (board[0][0] == 'X' && board[1][1] == 'X' && board[2][2] == 'X')  win = true; else
   if (board[0][0] == 'O' && board[1][1] == 'O' && board[2][2] == 'O')  win = true;

   if (board[0][2] == 'X' && board[1][1] == 'X' && board[2][0] == 'X')  win = true; else
   if (board[0][2] == 'O' && board[1][1] == 'O' && board[2][0] == 'O')  win = true;

   //cout << " win in check function " << win << endl;
   return win;
}


//The following print the board content
void printBoard(char board[][3])       //This function prints the board.
{
    cout << endl;
    for(int row=0; row <=2; row++)
    {
       for(int col=0; col <=2; col++)
       {
           cout << board[row][col];
       }
       cout << endl;
    }
    cout << endl;
}



//The following check whether the board content is a tie
bool checkTie(char board[][3])       //This function checks tie.
{

    int count = 0;
    for(int row=0; row <=2; row++)
    {
       for(int col=0; col <=2; col++)
       {
           if ((board [row][col] == 'O') || (board [row][col] == 'X'))  count++ ;
       }
    }
    if (count == 9) return true; else
                    return false;
}
