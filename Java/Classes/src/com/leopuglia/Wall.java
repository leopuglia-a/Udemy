public class Wall {
    // Fields
    private double width;
    private double height;

    // First constructor
    public Wall(){

    }
    // Second constructor
    public Wall(double width, double height){
        // conditions to be setting fields equal to zero
        if(width > 0 && height < 0){
            this.width = width;
            this.height = 0;
        }else if(width < 0 && height > 0){
            this.width = 0.0;
            this.height = height;
        }else if(width < 0 && height < 0){
            this.width = 0.0;
            this.height = 0.0;
        }else{
            this.width = width;
            this.height = height;
        }

    }
    // instance methods
    public double getWidth(){
        return this.width;
    }
    public double getHeight(){
        return this.height;
    }
    public void setWidth(double width){
        if(width < 0){
            this.width = 0;
        }else{
            this.width = width;
        }
    }
    public void setHeight(double height){
        if(height < 0){
            this.height = 0;
        }else{
            this.height = height;
        }
    }
    public double getArea(){
        return this.width * this.height; // Area of the wall
    }


}