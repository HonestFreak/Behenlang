

![image](https://user-images.githubusercontent.com/34571056/185396634-a3115f2b-1a93-4223-961c-512170673c2a.png)


Behenlang is a toy programming langauge inspired from Bhailang.

## Geting Started


### Prerequisites

You need llvmlite and sly modules to run the project.
* llvmlite
  ```sh
  pip install llvmlite
  ```

* sly
  ```sh
  pip install sly
  ```

## Usage

### Compiling the code

Extention for behenlang is .behen , to compile .behen files use
```sh
python run.py <filename.behen>
```

This will generate a .ll intermediate code file in the same folder where code is present and output the result too.


### Documentation:

#### General

<code>kaam</code> is used to define a function. One must define <code>main</code> function in the project. Example :
```sh
kaam int main() {
    # code goes here
    behen bhejo 0     #similar to return
}
```

<code>behen</code> or <code>didi</code> is used to initialize any statement.

#### Print

<code>behen bolo(<strings here>)</code> or <code>didi bolo(<strings here>)</code> is used to print the strings :
```sh
kaam int main() {

    didi bolo("Namste Duniya \n")
    behen bolo("Hello World")       #this is comment

    behen bhejo 0
}
```
  
#### Defining Variables

```sh
kaam int main() {

    behen x=5
    behen y=9.0
    
    behen bhejo 0
}
```

#### Conditional Statements

```sh
kaam int main() {

    behen num1 = 18
    behen rem = num1 % 2
    behen agar rem == 0{
        behen bolo('Even')
    } 
    warna{
        behen bolo('Odd')
    }

    behen bhejo 0
}

```
  
#### Iterations

```sh
kaam int main(){
    behen i = 0
    jabtak i < 10
    {
        didi bolo('Hello ')
        didi i = i+1
    }
   didi bhejo 0
    }

```
                 
#### Calling Functions

```sh
kaam int hello() {
    behen bolo("Ye hai hello function\n")
    behen bhejo 0
}

kaam int main(){
    hello()
    behen bolo("Ye hai main fun")
    behen bhejo 0
}

```




## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Dont forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


### Sources:

1. https://school.geekwall.in/p/Byz8Rg0GX
2. https://llvmlite.readthedocs.io/en/latest/
3. https://sly.readthedocs.io/en/latest/sly.html    #documentation enough to make lexer and parser. Can use other libs like rply too
4. https://groups.seas.harvard.edu/courses/cs153/2019fa/llvmlite.html
5. https://buildmedia.readthedocs.org/media/pdf/llvmlite/latest/llvmlite.pdf
6. https://github.com/topics/llvmlite   #reference from many projectes which used llvmlite

