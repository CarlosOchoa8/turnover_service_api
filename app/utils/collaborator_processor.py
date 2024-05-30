import re
from abc import ABC, abstractmethod
from typing import Any

import pandas as pd

from app.utils.classifier_model import clf_model


class CollaboratorProcessorStrategy(ABC):
    """Abstract class for collaborator adition strategy"""
    @abstractmethod
    def process_data(self, collaborators_data: Any):
        pass

    @abstractmethod
    def update_columns(self, collaborators_data: Any):
        pass


class SingleCollaborator(CollaboratorProcessorStrategy):
    """Concrete class for process a single collaborator data"""

    def process_data(self, collaborators_data: Any):
        """ 
        Select and drop column employee_column from data frame to predict
        properly.
        """
        model = clf_model.get_model()
        employee_number = collaborators_data['EmployeeNumber'][0]
        collaborators_data.drop(columns=['EmployeeNumber'], inplace=True)
        prediction = model.predict_proba(collaborators_data)
        return {'employee_number': employee_number,
                  'score': list(prediction[:, 1])[0]}

    def update_columns(self, collaborators_data: Any):
        """Update columns from of DataFrame from snake_case to CamelCase."""
        return [col.replace('_', ' ').title().replace(' ', '')
                for col in collaborators_data.columns]

class MultipleCollaborators(CollaboratorProcessorStrategy):
    """Concrete class for process multiple collaborators data"""
    columns = ['EmployeeCount',
                'Attrition',
                'JobLevel',
                'Over18',
                'StandardHours',
                'TotalWorkingYears']

    def process_data(self, collaborators_data: Any) -> list:
        """
        Drop columns from DataFrame and make the correspondic predict
        using the model
        """
        collaborators_data.drop(columns=self.columns, inplace=True)
        model = clf_model.get_model()
        collaborators_score = []

        for _, row in collaborators_data.iterrows():
            collaborator_json = row.to_dict()
            employee_number = collaborator_json.pop('EmployeeNumber')
            data_frame = pd.DataFrame([collaborator_json])
            prediction = model.predict_proba(data_frame)
            prediction_score = prediction[:, 1][0]
            collaborators_score.append({"employee_number": employee_number,
                                    "score": prediction_score})
        return collaborators_score

    def update_columns(self, collaborators_data: Any):
        """Update columns from of DataFrame from CamelCase to snake_case."""
        return [re.sub(r'(?<=[a-z])(?=[A-Z0-9])|(?<=[0-9])(?=[A-Z])', '_', col)
                                  .lower() for col in collaborators_data.columns]


multiple_collaborators = MultipleCollaborators()
single_collaborator = SingleCollaborator()
