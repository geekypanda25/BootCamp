package wc;

import java.io.IOException; 
import org.apache.hadoop.io.IntWritable; 
import org.apache.hadoop.io.LongWritable; 
import org.apache.hadoop.io.Text; 
import org.apache.hadoop.mapred.MapReduceBase; 
import org.apache.hadoop.mapred.Mapper; 
import org.apache.hadoop.mapred.OutputCollector; 
import org.apache.hadoop.mapred.Reporter; 
  
public class mapp extends MapReduceBase implements Mapper<LongWritable, Text, Text, IntWritable> 
{ 
  
    
    public void map(LongWritable key, Text value, OutputCollector<Text, IntWritable> out, Reporter rep) 
    { 
  
        String l = value.toString(); 
  
        for (String w : l.split(" "))  
        { 
            if (w.length() > 0) 
            { 
                out.collect(new Text(w), new IntWritable(1)); 
            } 
        } 
    } 
} 