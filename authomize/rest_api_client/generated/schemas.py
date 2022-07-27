# generated by datamodel-codegen:
#   filename:  openapi.json
#   timestamp: 2022-07-25T13:07:40+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field, constr


class AccessTypes(Enum):
    Unknown = 'Unknown'
    All = 'All'
    Owner = 'Owner'
    Read = 'Read'
    ReadMetadata = 'ReadMetadata'
    Write = 'Write'
    Create = 'Create'
    Delete = 'Delete'
    Execute = 'Execute'
    Enable = 'Enable'
    Assign = 'Assign'
    Restore = 'Restore'
    Import = 'Import'
    Export = 'Export'
    Get = 'Get'
    Set = 'Set'
    Update = 'Update'
    Cancel = 'Cancel'
    Use = 'Use'
    AllowUse = 'AllowUse'
    List = 'List'
    Administrative = 'Administrative'
    Delegate = 'Delegate'
    Join = 'Join'
    Invite = 'Invite'
    Leave = 'Leave'
    Share = 'Share'


class AssetTypes(Enum):
    Resource = 'Resource'
    File = 'File'
    Folder = 'Folder'
    Drive = 'Drive'
    Site = 'Site'
    Application = 'Application'
    Integration = 'Integration'
    Package = 'Package'
    Project = 'Project'
    Cluster = 'Cluster'
    Dataset = 'Dataset'
    Subscription = 'Subscription'
    Table = 'Table'
    TableRecord = 'TableRecord'
    Disk = 'Disk'
    Image = 'Image'
    Instance = 'Instance'
    Snapshot = 'Snapshot'
    Service = 'Service'
    Topic = 'Topic'
    Bucket = 'Bucket'
    BillingAccount = 'BillingAccount'
    Device = 'Device'
    Calendar = 'Calendar'
    Policy = 'Policy'
    GitRepository = 'GitRepository'
    Network = 'Network'
    Vpc = 'Vpc'
    NetworkInterface = 'NetworkInterface'
    VirtualMachine = 'VirtualMachine'
    NetworkSecurityGroup = 'NetworkSecurityGroup'
    Ticket = 'Ticket'
    NetworkSubnet = 'NetworkSubnet'
    NetworkAcl = 'NetworkAcl'
    RouteTable = 'RouteTable'
    NetworkAddress = 'NetworkAddress'
    Secret = 'Secret'
    Storage = 'Storage'
    Workspace = 'Workspace'
    SharedLink = 'SharedLink'
    Collection = 'Collection'
    Database = 'Database'
    ServerlessFunction = 'ServerlessFunction'
    ServerlessApplication = 'ServerlessApplication'
    Gateway = 'Gateway'
    ImageRepository = 'ImageRepository'
    Resource_BusinessAccount = 'Resource_BusinessAccount'
    LoadBalancer = 'LoadBalancer'
    Listener = 'Listener'


class AssetsInheritance(BaseModel):
    fromId: str = Field(..., title='Fromid')
    toId: str = Field(..., title='Toid')


class AvailableConnectorId(Enum):
    restApiImport = 'restApiImport'


class ConnectorStatus(Enum):
    initializing = 'initializing'
    validating = 'validating'
    failure = 'failure'
    enabled = 'enabled'
    installable = 'installable'
    archived = 'archived'
    disabled = 'disabled'
    deleted = 'deleted'


class ExportResponse(BaseModel):
    exportId: str = Field(..., title='Exportid')
    exportUrl: str = Field(..., title='Exporturl')


class IdentitiesInheritance(BaseModel):
    fromId: str = Field(..., title='Fromid')
    toId: str = Field(..., title='Toid')


class IdentityTypes(Enum):
    Identity = 'Identity'
    User = 'User'
    Group = 'Group'
    EntitlementProxy = 'EntitlementProxy'
    AccessKey = 'AccessKey'
    ServiceAccount = 'ServiceAccount'
    Alias = 'Alias'
    Domain = 'Domain'
    Organization = 'Organization'
    TaskPerformer = 'TaskPerformer'
    BusinessAccount = 'BusinessAccount'


class IsAliveResponse(BaseModel):
    isAlive: bool = Field(..., title='Isalive')


class MeResponse(BaseModel):
    version: str = Field(..., title='Version')
    id: str = Field(..., title='Id')
    tenant: str = Field(..., title='Tenant')


class NewGroupMembersRequestSchema(BaseModel):
    groupId: str = Field(..., description="he members' group id", title='Groupid')
    members: List[str] = Field(
        ...,
        description='List of the new members ids, expected to be existing members',
        title='Members',
    )


class NewGroupMembersResponseSchema(BaseModel):
    acceptedTimestamp: datetime = Field(..., title='Acceptedtimestamp')
    requestId: str = Field(..., title='Requestid')
    numberOfAcceptedMembers: Optional[int] = Field(
        "The number of groups' members that pass validation and uploaded",
        title='Numberofacceptedmembers',
    )


class NewGroupRequestSchema(BaseModel):
    id: str = Field(..., description='Group id', title='Id')
    name: str = Field(..., description='Group name', title='Name')
    tags: Optional[List[str]] = Field(None, description='Tags', title='Tags')


class NewGroupResponseSchema(BaseModel):
    acceptedTimestamp: datetime = Field(..., title='Acceptedtimestamp')
    requestId: str = Field(..., title='Requestid')
    numberOfAcceptedGroups: Optional[int] = Field(
        'The number of groups that pass validation and uploaded', title='Numberofacceptedgroups'
    )


class NewRestApiConnectorSchema(BaseModel):
    config: Optional[Dict[str, Any]] = Field(None, title='Config')
    serviceId: constr(min_length=1) = Field(..., title='Serviceid')


class NewUserResponseSchema(BaseModel):
    acceptedTimestamp: datetime = Field(..., title='Acceptedtimestamp')
    requestId: str = Field(..., title='Requestid')
    numberOfAcceptedUsers: int = Field(
        ...,
        description='The number of users that pass validation and uploaded',
        title='Numberofacceptedusers',
    )


class Pagination(BaseModel):
    limit: Optional[int] = Field(-1, title='Limit')
    skip: Optional[int] = Field(0, title='Skip')
    total: Optional[int] = Field(-1, title='Total')
    hasMore: Optional[bool] = Field(None, title='Hasmore')


class RestApiConnectorSchema(BaseModel):
    config: Optional[Dict[str, Any]] = Field(None, title='Config')
    serviceId: Optional[str] = Field('', title='Serviceid')
    id: str = Field(..., title='Id')
    createdAt: Optional[datetime] = Field(None, title='Createdat')
    lastSyncedAt: Optional[str] = Field(None, title='Lastsyncedat')
    lastError: Optional[str] = Field(None, title='Lasterror')
    modifiedAt: Optional[str] = Field(None, title='Modifiedat')
    status: Optional[ConnectorStatus] = 'disabled'
    serviceType: str = Field(..., title='Servicetype')
    availableConnectorId: Optional[AvailableConnectorId] = 'restApiImport'
    actorType: Optional[str] = Field(None, title='Actortype')
    actorId: Optional[str] = Field(None, title='Actorid')


class ServiceDescription(BaseModel):
    name: str = Field(..., title='Name')
    icon: Optional[str] = Field(None, title='Icon')


class SubmitResponse(BaseModel):
    acceptedTimestamp: datetime = Field(..., title='Acceptedtimestamp')


class TransactionStateType(Enum):
    Applying = 'Applying'
    Complete = 'Complete'
    Failed = 'Failed'
    Ingest = 'Ingest'
    IngestChunk = 'IngestChunk'
    PostProcess = 'PostProcess'
    Queue = 'Queue'


class UserStatus(Enum):
    Staged = 'Staged'
    Enabled = 'Enabled'
    Disabled = 'Disabled'
    Suspended = 'Suspended'
    Deleted = 'Deleted'
    Unknown = 'Unknown'


class ValidationError(BaseModel):
    loc: List[str] = Field(..., title='Location')
    msg: str = Field(..., title='Message')
    type: str = Field(..., title='Error Type')


class AccessDescription(BaseModel):
    fromIdentityId: str = Field(..., title='Fromidentityid')
    toAssetId: str = Field(..., title='Toassetid')
    accessType: AccessTypes
    accessName: Optional[str] = Field(None, title='Accessname')


class AssetDescription(BaseModel):
    id: str = Field(..., title='Id')
    name: str = Field(..., title='Name')
    type: AssetTypes
    description: Optional[str] = Field(None, title='Description')
    logoUrl: Optional[str] = Field(None, title='Logourl')
    href: Optional[str] = Field(None, title='Href')
    createdAt: Optional[datetime] = Field(None, title='Createdat')
    isAuxiliary: Optional[bool] = Field(None, title='Isauxiliary')
    isFederated: Optional[bool] = Field(None, title='isFederated')
    service: Optional[str] = Field(None, title='Service')


class BundleTransactionSchema(BaseModel):
    connectorId: str = Field(..., title='Connectorid')
    transactionCreatedAt: Optional[datetime] = Field(None, title='Transactioncreatedat')
    warnings: Optional[List[str]] = Field(None, title='Warnings')
    validations: Optional[Dict[str, Any]] = Field(None, title='Validations')
    id: str = Field(..., title='Id')
    state: TransactionStateType


class HTTPValidationError(BaseModel):
    detail: Optional[List[ValidationError]] = Field(None, title='Detail')


class IdentityDescription(BaseModel):
    id: str = Field(..., title='Id')
    name: Optional[str] = Field(None, title='Name')
    type: IdentityTypes
    userType: Optional[str] = Field(None, title='Usertype')
    email: Optional[str] = Field(None, title='Email')
    manager: Optional[str] = Field(None, title='Manager')
    title: Optional[str] = Field(None, title='Title')
    department: Optional[str] = Field(None, title='Department')
    description: Optional[str] = Field(None, title='Description')
    href: Optional[str] = Field(None, title='Href')
    createdAt: Optional[datetime] = Field(None, title='Createdat')
    terminationDate: Optional[datetime] = Field(None, title='Terminationdate')
    isExternal: Optional[bool] = Field(None, title='Isexternal')
    isAuxiliary: Optional[bool] = Field(None, title='Isauxiliary')
    hasTwoFactorAuthenticationEnabled: Optional[bool] = Field(
        None, title='Hastwofactorauthenticationenabled'
    )
    firstName: Optional[str] = Field(None, title='Firstname')
    lastName: Optional[str] = Field(None, title='Lastname')
    userName: Optional[str] = Field(None, title='Username')
    status: Optional[UserStatus] = None
    service: Optional[str] = Field(None, title='Service')
    lastLoginDate: Optional[datetime] = Field(None, title='Lastlogindate')
    tags: Optional[List[str]] = Field(None, title='Tags')


class ItemsBundleSchema(BaseModel):
    services: Optional[List[ServiceDescription]] = Field(None, title='Services')
    identities: List[IdentityDescription] = Field(..., title='Identities')
    assets: List[AssetDescription] = Field(..., title='Assets')
    inheritanceIdentities: List[IdentitiesInheritance] = Field(..., title='Inheritanceidentities')
    inheritanceAssets: List[AssetsInheritance] = Field(..., title='Inheritanceassets')
    access: List[AccessDescription] = Field(..., title='Access')


class NewUserRequestSchema(BaseModel):
    id: str = Field(..., description='User ID', title='Id')
    name: Optional[str] = Field(None, description='User name', title='Name')
    email: Optional[str] = Field(None, description='User email', title='Email')
    firstName: Optional[str] = Field(None, description='User first name', title='Firstname')
    lastName: Optional[str] = Field(None, description='User last name', title='Lastname')
    status: Optional[UserStatus] = Field(None, description='User status')
    description: Optional[str] = Field(
        None, description='Description of the user', title='Description'
    )
    isExternal: Optional[bool] = Field(
        None, description='If the user been imported from external integration', title='Isexternal'
    )
    hasTwoFactorAuthenticationEnabled: Optional[bool] = Field(
        None, description='If the user has MFA', title='Hastwofactorauthenticationenabled'
    )
    lastLoginDate: Optional[datetime] = Field(
        None, description='Last time the user login into the system', title='Lastlogindate'
    )
    tags: Optional[List[str]] = Field(None, description='Tags', title='Tags')


class RestApiConnectorListSchema(BaseModel):
    pagination: Pagination
    data: List[RestApiConnectorSchema] = Field(..., title='Data')


class TransactionPaginatedSearchSchema(BaseModel):
    data: List[BundleTransactionSchema] = Field(..., title='Data')
    pagination: Pagination
