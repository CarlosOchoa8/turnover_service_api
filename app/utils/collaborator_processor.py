import re
from abc import ABC, abstractmethod
from typing import Any

import joblib
import pandas as pd


class CollaboratorProcessor(ABC):

    @abstractmethod
    def process_data(self, collaborators_data: Any):
        pass

    @abstractmethod
    def update_columns(self, collaborators_data: Any):
        pass


class SingleCollaborator(CollaboratorProcessor):
    """Concrete class for process a single collaborator data"""
    fields = [
            'employee_count',
            'attrition',
            'job_level',
            'over18',
            'standard_hours',
            'total_working_years']

    def process_data(self, collaborators_data: Any):
        clf_model = joblib.load("clf.zahoree")
        employee_number = collaborators_data['EmployeeNumber'][0]
        collaborators_data.drop(columns=['EmployeeNumber'], inplace=True)
        prediction = clf_model.predict_proba(collaborators_data)
        return {'employee_number': employee_number,
                  'score': list(prediction[:, 1])[0]}

    def update_columns(self, collaborators_data: Any):
        return [col.replace('_', ' ').title().replace(' ', '')
                for col in collaborators_data.columns]

class MultipleCollaborators(CollaboratorProcessor):
    """Concrete class for process multiple collaborators data"""
    columns = ['EmployeeCount',
                'Attrition',
                'JobLevel',
                'Over18',
                'StandardHours',
                'TotalWorkingYears']

    def process_data(self, collaborators_data: Any) -> list:
        collaborators_data.drop(columns=self.columns, inplace=True)
        clf_model = joblib.load("clf.zahoree")
        collaborators_score = []

        for _, row in collaborators_data.iterrows():
            collaborator_json = row.to_dict()
            employee_number = collaborator_json.pop('EmployeeNumber')
            data_frame = pd.DataFrame([collaborator_json])
            prediction = clf_model.predict_proba(data_frame)
            prediction_score = prediction[:, 1][0]
            collaborators_score.append({"employee_number": employee_number,
                                    "score": prediction_score})
        return collaborators_score

    def update_columns(self, collaborators_data: Any):
        return [re.sub(r'(?<=[a-z])(?=[A-Z0-9])|(?<=[0-9])(?=[A-Z])', '_', col)
                                  .lower() for col in collaborators_data.columns]


multiple_collaborators = MultipleCollaborators()
single_collaborator = SingleCollaborator()
