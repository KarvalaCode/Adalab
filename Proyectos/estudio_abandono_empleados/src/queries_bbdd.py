
query_creacion_bbdd = "CREATE SCHEMA IF NOT EXISTS `empleados` DEFAULT CHARACTER SET utf8;"

query_tabla_datos_personales = """
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
                    """
                    
query_tabla_empresa = """
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
                    """

query_tabla_salarios = """ 
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
                    """

query_tabla_valoraciones = """ 
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
                """
                            
query_insertar_datos_personales = "INSERT INTO datos_personales (employee_number, age, date_birth, gender, marital_status, distance_from_home, num_companies_worked, total_working_years, education, education_field) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

query_insertar_valoraciones = "INSERT INTO valoraciones (employee_number, environment_satisfaction, job_involvement, job_satisfaction, performance_rating, relationship_satisfaction, work_life_balance, datos_personales_employee_number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"


query_insertar_salarios = "INSERT INTO salarios (employee_number, monthly_rate, percent_salary_hike, hourly_rate, daily_rate, monthly_income, datos_personales_employee_number) VALUES (%s, %s, %s, %s, %s, %s, %s)"

query_insertar_empresa = "INSERT INTO gestion_interna_empresa (employee_number, attrition, business_travel, department, job_level, job_role, overtime, stock_option_level, training_times_last_year, years_at_company, years_since_last_promotion, years_with_curr_manager, remote_work, datos_personales_employee_number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"