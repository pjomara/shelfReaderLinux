#This is the call_parser for DVDs

def main():
    call= "dvd 150 "   
    parse_call= call_parser(call)

def call_parser(call):
    call = call.rstrip()
    if call[0] == "4":
        call = call[6:]
    else:
        call = call[4:]

    if "oversize" in call:
        call = "oversize"+call[0:len(call)-8]

    return call

main()
