=begin
#ORY Keto

#Ory Keto is a cloud native access control server providing best-practice patterns (RBAC, ABAC, ACL, AWS IAM Policies, Kubernetes Roles, ...) via REST APIs.

The version of the OpenAPI document: v0.7.0-alpha.0
Contact: hi@ory.sh
Generated by: https://openapi-generator.tech
OpenAPI Generator version: 5.2.1

=end

require 'spec_helper'
require 'json'

# Unit tests for OryKetoClient::WriteApi
# Automatically generated by openapi-generator (https://openapi-generator.tech)
# Please update as you see appropriate
describe 'WriteApi' do
  before do
    # run before each test
    @api_instance = OryKetoClient::WriteApi.new
  end

  after do
    # run after each test
  end

  describe 'test an instance of WriteApi' do
    it 'should create an instance of WriteApi' do
      expect(@api_instance).to be_instance_of(OryKetoClient::WriteApi)
    end
  end

  # unit tests for create_relation_tuple
  # Create a Relation Tuple
  # Use this endpoint to create a relation tuple.
  # @param [Hash] opts the optional parameters
  # @option opts [RelationQuery] :payload 
  # @return [RelationQuery]
  describe 'create_relation_tuple test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for delete_relation_tuple
  # Delete a Relation Tuple
  # Use this endpoint to delete a relation tuple.
  # @param namespace Namespace of the Relation Tuple
  # @param object Object of the Relation Tuple
  # @param relation Relation of the Relation Tuple
  # @param [Hash] opts the optional parameters
  # @option opts [String] :subject_id SubjectID of the Relation Tuple
  # @option opts [String] :subject_set_namespace Namespace of the Subject Set
  # @option opts [String] :subject_set_object Object of the Subject Set
  # @option opts [String] :subject_set_relation Relation of the Subject Set
  # @return [nil]
  describe 'delete_relation_tuple test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for patch_relation_tuples
  # Patch Multiple Relation Tuples
  # Use this endpoint to patch one or more relation tuples.
  # @param [Hash] opts the optional parameters
  # @option opts [Array<PatchDelta>] :payload 
  # @return [nil]
  describe 'patch_relation_tuples test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

end
