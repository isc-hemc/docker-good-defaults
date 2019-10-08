class MyClass {
  private hello: string;

  constructor(hello: string) {
    this.hello = hello;
  }

  get getHello(): string {
    return this.hello;
  }
}

const myClass = new MyClass("Hello David");
console.log(myClass.getHello);
