import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

def run():
    #Pipeline configuration

    options = PipelineOptions(
        # runner="DirectRunner",  # Use 'DirectRunner' for running on localhost
        runner="DataflowRunner",  # Use 'DataflowRunner' for running on Google Cloud Dataflow
        project= "gcp-data-engineer-course03",
        region= "us-central1",
        temp_location="gs://gcs-bucket-course-05/temp",
    )

    with beam.Pipeline(options=options) as p:
        (
            p
            | "Read file" >> beam.io.ReadFromText("gs://dataflow-samples/shakespeare/kinglear.txt")
            | "split words" >> beam.FlatMap(lambda line: line.split())
            | "Count words" >> beam.combiners.Count.PerElement()
            | "Save results" >> beam.io.WriteToText("gs://gcs-bucket-course-05/output/wordcount")
        )

    print("Pipeline executed properly.")

if __name__ == "__main__":    
    run()
