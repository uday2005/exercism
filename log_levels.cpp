
#include <string>
 
namespace log_line {
    std::string message(std::string line) {
        int why = line.find(" ");
        std::string why2 = line.substr(why+1);
        return why2;
    }

    std::string log_level(std::string line) {
        int why = line.find("]");
        std::string why2 = line.substr(1,why-1);
        return why2;
        
    }

    std::string reformat(std::string line) {
     int why = line.find("]");
    std::string why2 = line.substr(1,why-1);
    std::string why3 = line.substr(why+3);
    std::string fin = why3 + " " + "(" + why2 + ")";
        return fin;
    }
}