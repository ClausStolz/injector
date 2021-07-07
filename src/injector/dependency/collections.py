from abc import ABC, abstractmethod
from typing import Any, Optional


class Collection(ABC):
    """
    Helper class to implement abstract entity for all
    dependency collection subclasses.
    """
    @abstractmethod
    def add(
        self,
        key: type,
        value: Optional[Any] = None
    ) -> None:
        """
        Method to add type or value in collection. 
        Default adding is using type in argument for creating 
        object to injection. If need to use special object to 
        inject, is way here to creating this object via value 
        in argument.

        Args:
            key (type): type that need to be injection.
            value (Optional[object], optional): special object 
            to injection. Defaults to None.

        Usage:
            my_collection.add(MyReferenceType1)
                or
            my_collection.add(int, 10) #bad way to inject value
            type, using only to show how adding via value argument
        """


    @abstractmethod
    def get(
        self, 
        key: type
    ) -> Any:
        """
        Method to get object to inject via type.

        Args:
            key (type): type that need to be injection.

        Returns:
            Any: injection object from collection.

        Usage:
            my_collection.get(MyReferenceType)
        """
