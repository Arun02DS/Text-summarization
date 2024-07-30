from src.TextSummariser.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipepline
from src.TextSummariser.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.TextSummariser.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from src.TextSummariser.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from src.TextSummariser.pipeline.stage_05_data_evaluation import ModelEvaluationTrainingPipeline
from src.TextSummariser.logging import logger


STAGE_NAME='Data Ingestion Stage'

try:
    logger.info(f"{'>>>'*10} stage : {STAGE_NAME} started {'<<<'*10}")
    data_ingestion=DataIngestionTrainingPipepline()
    data_ingestion.main()
    logger.info(f"{'>>>'*10} stage : {STAGE_NAME} completed {'<<<'*10}")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME='Data Validation Stage'

try:
    logger.info(f"{'>>>'*10} stage : {STAGE_NAME} started {'<<<'*10}")
    data_validation=DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f"{'>>>'*10} stage : {STAGE_NAME} completed {'<<<'*10}")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME='Data Transformation Stage'

try:
    logger.info(f"{'>>>'*10} stage : {STAGE_NAME} started {'<<<'*10}")
    data_transformation=DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f"{'>>>'*10} stage : {STAGE_NAME} completed {'<<<'*10}")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME='Model Trainer Stage'

try:
    logger.info(f"{'>>>'*10} stage : {STAGE_NAME} started {'<<<'*10}")
    model_trainer=ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info(f"{'>>>'*10} stage : {STAGE_NAME} completed {'<<<'*10}")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME='Model Evaluation Stage'

try:
    logger.info(f"{'>>>'*10} stage : {STAGE_NAME} started {'<<<'*10}")
    model_eval=ModelEvaluationTrainingPipeline
    model_eval.main()
    logger.info(f"{'>>>'*10} stage : {STAGE_NAME} completed {'<<<'*10}")
except Exception as e:
    logger.exception(e)
    raise e


