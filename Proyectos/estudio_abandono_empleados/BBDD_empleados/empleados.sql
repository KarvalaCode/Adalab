-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema empleados
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema empleados
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `empleados` DEFAULT CHARACTER SET utf8 ;
USE `empleados` ;

-- -----------------------------------------------------
-- Table `empleados`.`datos_personales`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `empleados`.`datos_personales` (
  `employee_number` INT NOT NULL,
  `age` INT NOT NULL,
  `date_birth` INT NULL DEFAULT NULL,
  `gender` VARCHAR(45) NULL DEFAULT NULL,
  `marital_status` VARCHAR(45) NULL DEFAULT NULL,
  `distance_from_home` FLOAT NULL DEFAULT NULL,
  `num_companies_worked` INT NULL DEFAULT NULL,
  `total_working_years` INT NULL DEFAULT NULL,
  `education` VARCHAR(45) NULL DEFAULT NULL,
  `education_field` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`employee_number`),
  UNIQUE INDEX `employee_number_UNIQUE` (`employee_number` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `empleados`.`gestion_interna_empresa`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `empleados`.`gestion_interna_empresa` (
  `employee_number` INT NOT NULL,
  `attrition` VARCHAR(45) NULL DEFAULT NULL,
  `business_travel` VARCHAR(45) NULL DEFAULT NULL,
  `department` VARCHAR(45) NULL DEFAULT NULL,
  `job_level` INT NULL DEFAULT NULL,
  `job_role` VARCHAR(45) NULL DEFAULT NULL,
  `overtime` VARCHAR(45) NULL DEFAULT NULL,
  `stock_option_level` INT NULL DEFAULT NULL,
  `training_times_last_year` INT NULL DEFAULT NULL,
  `years_at_company` INT NULL DEFAULT NULL,
  `years_since_last_promotion` INT NULL DEFAULT NULL,
  `years_with_curr_manager` INT NULL DEFAULT NULL,
  `remote_work` VARCHAR(45) NULL DEFAULT NULL,
  `datos_personales_employee_number` INT NOT NULL,
  PRIMARY KEY (`employee_number`),
  UNIQUE INDEX `employee_number_UNIQUE` (`employee_number` ASC) VISIBLE,
  INDEX `fk_gestión_interna_empresa_datos_personales_idx` (`datos_personales_employee_number` ASC) VISIBLE,
  CONSTRAINT `fk_gestión_interna_empresa_datos_personales`
    FOREIGN KEY (`datos_personales_employee_number`)
    REFERENCES `empleados`.`datos_personales` (`employee_number`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `empleados`.`salarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `empleados`.`salarios` (
  `employee_number` INT NOT NULL,
  `monthly_rate` INT NULL DEFAULT NULL,
  `percent_salary_hike` INT NULL DEFAULT NULL,
  `hourly_rate` FLOAT NULL DEFAULT NULL,
  `daily_rate` FLOAT NULL DEFAULT NULL,
  `monthly_income` FLOAT NULL DEFAULT NULL,
  `datos_personales_employee_number` INT NOT NULL,
  PRIMARY KEY (`employee_number`),
  UNIQUE INDEX `employee_number_UNIQUE` (`employee_number` ASC) VISIBLE,
  INDEX `fk_salarios_datos_personales1_idx` (`datos_personales_employee_number` ASC) VISIBLE,
  CONSTRAINT `fk_salarios_datos_personales1`
    FOREIGN KEY (`datos_personales_employee_number`)
    REFERENCES `empleados`.`datos_personales` (`employee_number`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `empleados`.`valoraciones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `empleados`.`valoraciones` (
  `employee_number` INT NOT NULL,
  `environment_satisfaction` INT NULL DEFAULT NULL,
  `job_involvement` INT NULL DEFAULT NULL,
  `job_satisfaction` INT NULL DEFAULT NULL,
  `performance_rating` FLOAT NULL DEFAULT NULL,
  `relationship_satisfaction` INT NULL DEFAULT NULL,
  `work_life_balance` FLOAT NULL DEFAULT NULL,
  `datos_personales_employee_number` INT NOT NULL,
  PRIMARY KEY (`employee_number`),
  UNIQUE INDEX `employee_number_UNIQUE` (`employee_number` ASC) VISIBLE,
  INDEX `fk_valoraciones_datos_personales1_idx` (`datos_personales_employee_number` ASC) VISIBLE,
  CONSTRAINT `fk_valoraciones_datos_personales1`
    FOREIGN KEY (`datos_personales_employee_number`)
    REFERENCES `empleados`.`datos_personales` (`employee_number`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
