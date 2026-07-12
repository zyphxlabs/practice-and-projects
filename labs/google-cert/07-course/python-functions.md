## Google Cybersecurity Certificate Course 7 Python For Cybersecurity
### Lab Define And Call A Function


## What This Lab Covered
This lab was about defining and calling functions in Python which is basically how you package up a block of code so you can reuse it instead of writing the same thing over and over. The scenario had me building an alert() function to flag potential security issues and a list_to_string() function to convert a list of approved usernames into one readable string.

## What I Actually Did
I started by analyzing an already defined alert() function that just printed Potential security issue. Investigate further. when called. I called it myself and got that exact message back on the screen which made sense since defining a function on its own does not actually run anything until you call it.

After this when I came to the part which they lack that was when things started to seems bad because the second version of alert() wrapped the same print statement inside a for loop using range(3) so instead of printing the message once it printed Potential security issue. Investigate further. three separate times when I called it. That showed me how easily you can combine things I already learned like loops directly inside a function body.

Then I moved into building list_to_string() from scratch starting with just the function header using def and a colon. After analyzing that I filled in the body with a username_list containing eight approved usernames elarson bmoreno tshah sgilmore eraab gesparza alevitsk and wjaffrey and wrote a for loop inside the function that looped through and printed each username one at a time on its own line.

Next I rebuilt that same function but this time instead of just printing each username individually I used string concatenation with the + operator to combine every username into a single variable called sum_variable which started out as an empty string. When I called the function and printed sum_variable at the end all eight usernames were mashed together into one long unreadable line that read elarsonbmorenotshahsgilmoreeraabgesparzaalevitskwjaffrey with no spacing at all.

That was when I fixed it by adding a comma and a space after each username inside the loop so instead of just adding i to sum_variable I added i plus ", " each time. Running it after that gave me elarson bmoreno tshah sgilmore eraab gesparza alevitsk wjaffrey each separated cleanly by a comma and a space which was way easier to actually read and made we understand why formatting matters just as much as getting the logic right.

## Key Takeaways
- functions let you package up code so you can reuse it instead of rewriting the same block every time
- a function has to be called after its defined or nothing happens even if the definition itself runs with no errors
- you can nest things like for loops inside a function body the same way you would use them anywhere else
- string concatenation with + is how you combine multiple strings into one but without proper spacing the result is hard to read
- small formatting choices like adding a comma and space after each item can completely change how usable the output actually is

Completed as part of the Google Cybersecurity Certificate program.