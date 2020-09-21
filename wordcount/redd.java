package wc;

import java.io.IOException; 
import java.util.Iterator; 
import org.apache.hadoop.io.IntWritable; 
import org.apache.hadoop.io.Text; 
import org.apache.hadoop.mapred.MapReduceBase; 
import org.apache.hadoop.mapred.OutputCollector; 
import org.apache.hadoop.mapred.Reducer; 
import org.apache.hadoop.mapred.Reporter; 
  
public class redd extends MapReduceBase implements Reducer<Text, IntWritable, Text, IntWritable> 
{ 
   
    public void reduce(Text key, Iterator<IntWritable> value, OutputCollector<Text, IntWritable> out,  Reporter rep) 
    { 
  
        int ct = 0; 
  
        while (value.hasNext())  
        { 
            IntWritable i = value.next(); 
            ct += i.get(); 
        } 
  
        out.collect(key, new IntWritable(count)); 
    } 
} 